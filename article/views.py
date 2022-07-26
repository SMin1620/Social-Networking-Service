import socket
from elasticsearch import Elasticsearch

from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import (
    IsAdminUser,
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from django.db.models import Q, F, Count, Case, When
from django.shortcuts import get_object_or_404
from django.core.cache import cache
from django.db import transaction

from article.models import (
    Article,
    ArticleLikedUser
)
from article.serializers import (
    ArticleListCreateSerializer,
    ArticleDetailSerializer,
    ArticleUpdateDeleteSerializer,
    ArticleRestoreSerializer
)
from SNS.drf.swagger import (
    param_hashtags,
    param_search,
    param_orderby,
)
from SNS.drf.pagination import ArticlePageNumberPagination
from SNS.drf.permissions import IsOwnerOrReadOnly


# Create your views here.
class ArticleListCreateViewSet(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               viewsets.GenericViewSet):
    """
    게시글 조회 - 모든 사용자 접근 가능
             - 해시태그 필터링
    게시글 생성 - 인가된 사용자만 접근 가능
    사용자 전용 뷰셋
    """
    queryset = Article.objects.all()
    serializer_class = ArticleListCreateSerializer
    pagination_class = ArticlePageNumberPagination
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        if self.action == 'list':
            hashtags = self.request.GET.get('hashtags', '')             # 해시태그 입력
            search = self.request.GET.get('search', '')                # 검색 단어 입력
            orderby = self.request.GET.get('orderby', 'created_at')   # 정렬 단어 입력

            # elasticsearch
            elasticsearch = Elasticsearch(
                settings.ELASTIC_HOST, http_auth=(settings.ELASTIC_ID, settings.ELASTIC_PW), )

            elastic_sql = f"""
                SELECT id
                FROM sns
                WHERE 1=1
                """

            condition = Q()
            if hashtags:    # 입력받은 해시태그 파라미터가 있다면,
                # CASE 1 : django Q를 이용한 방식
                # condition.add(
                #     Q(tags__name__in=hashtags),
                #     Q.OR
                # )
                # CASE 2 : 엘라스틱 서치 쿼리를 이용한 방식
                elastic_sql += f"""
                AND
                (
                    MATCH(hashtags_nori, '{hashtags}')  
                )
                """

            if search:
                # CASE 1 : django Q를 이용한 방식
                # condition.add(
                #     Q(title__icontains=search) |
                #     Q(content__icontains=search),
                #     Q.OR
                # )

                # CASE 2 : 엘라스틱 서치 쿼리를 이용한 방식
                elastic_sql += f"""
                AND
                (
                    MATCH(title_nori, '{search}')
                    OR
                    MATCH(content_nori, '{search}')
                )
                """

            if orderby:
                # CASE : 엘라스틱 서치 쿼리를 이용한 방식
                elastic_sql += f"""ORDER BY {orderby}"""

            response = elasticsearch.sql.query(body={"query": elastic_sql})
            article_ids = [row[0] for row in response['rows']]

            order = Case(*[When(id=id, then=art) for art, id in enumerate(article_ids)])

            queryset = Article.objects.filter(id__in=article_ids).order_by(order)
            return queryset

        else:
            return Article.objects.all()

    def get_serializer_class(self):
        return ArticleListCreateSerializer

    @swagger_auto_schema(manual_parameters=[param_hashtags, param_search, param_orderby])
    def list(self, request, *args, **kwargs):
        """
        게시글 목록 조회
        사용자 전용
        스웨거 데코레이터를 이용하기 위해서 선언함
        """
        return super().list(request, *args, **kwargs)

    @transaction.atomic()
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ArticleDetailUpdateDeleteViewSet(mixins.RetrieveModelMixin,
                                       mixins.UpdateModelMixin,
                                       mixins.DestroyModelMixin,
                                       viewsets.GenericViewSet):
    """
    게시글 상세 조회 - 모든 사용자 접근 가능
    게시글 수정 - 본인만 접근 가능
    게시글 삭제 - 본인만 접근 가능
    사용자 전용 뷰셋
    """
    lookup_url_kwarg = 'article_id'
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Article.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleDetailSerializer
        else:
            return ArticleUpdateDeleteSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs['article_id']
        article = get_object_or_404(Article, pk=pk)
        expire_time = 600  # 조회수 설정 시간 10분

        user = request.user.id
        if user is None:    # 인가되지 않은 사용자 (게스트)
            user = socket.gethostbyname(socket.gethostname())

        # 캐싱을 이용해서 조회수 기능 구현
        cache_value = cache.get(f'user-{user}', '_')
        response = Response(status=status.HTTP_200_OK)

        # 인가된 사용자의 조회수 증가
        if f'_{pk}_' not in cache_value:
            cache_value += f'{pk}_'
            cache.set(f'user-{user}', cache_value, expire_time)
            article.hits += 1
            article.save()

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response.data = serializer.data
        return response

    def partial_update(self, request, *args, **kwargs):
        """
        게시글 부분 수정
        본인만 접근 가능
        사용자 전용
        """
        kwargs['partial'] = True

        return self.update(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    def like(self, request, *args, **kwargs):
        """
        좋아요 추가, 삭제 - 인가된 사용자만 가능
        사용자 전용
        """
        pk = kwargs['article_id']
        user = request.user
        article = get_object_or_404(Article, pk=pk)

        if article.article_liked_user.filter(pk=pk).exists():   # 해당 게시글에 유저가 이미 좋아요를 했다면,
            article.article_liked_user.remove(user.id)          # 좋아요 취소
        else:                                                   # 해당 게시글에 유저가 좋아요를 하지 않았다면,
            article.article_liked_user.add(user.id)             # 좋아요 추가

        return Response(status=status.HTTP_200_OK)


class ArticleRestoreViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    """
    삭제한 게시글 목록 조회
    삭제한 게시글 상세 조회
    게시글 삭제 복구 뷰셋
    """
    lookup_url_kwarg = 'article_id'
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Article.deleted_objects.all()

    def get_serializer_class(self):
        return ArticleRestoreSerializer

    @action(detail=True, methods=['patch'])
    def restore(self, request, *args, **kwargs):
        """
        삭제된 게시글 복구
        사용자 전용
        """
        pk = kwargs['article_id']
        article = Article.deleted_objects.get(pk=pk)
        article.restore()

        return Response(status=status.HTTP_200_OK)




