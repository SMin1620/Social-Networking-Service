from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from django.db.models import Q, F, Count

from article.models import (
    Article,
    ArticleLikedUser
)
from article.serializers import (
    ArticleListCreateSerializer,
    ArticleDetailSerializer,
    ArticleUpdateDeleteSerializer
)
from SNS.drf.swagger import (
    param_hashtags,
    param_search,
    param_orderby,
)


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

    def get_queryset(self):
        if self.action == 'list':
            hashtag = self.request.GET.get('hashtags', '')             # 해시태그 입력
            search = self.request.GET.get('search', '')                # 검색 단어 입력
            orderby = self.request.GET.get('orderby', '-created_at')   # 정렬 단어 입력

            hashtags = hashtag and hashtag.split(' ') and hashtag.split(',')    # 해시태그 필터
            set_order_by = [
                'created_at',
                '-created_at',
                'hits',
                '-hits',
                'article_liked_user',
                '-article_liked_user'
            ]

            condition = Q()
            if hashtags:    # 입력받은 해시태그 파라미터가 있다면,
                condition.add(
                    Q(tags__name__in=hashtags),
                    Q.OR
                )
            if search:
                condition.add(
                    Q(title__icontains=search) |
                    Q(content__icontains=search),
                    Q.OR
                )
            if orderby in set_order_by:
                queryset = Article.objects.filter(condition).order_by(orderby).distinct()

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
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


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

    def get_queryset(self):
        return Article.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleDetailSerializer
        else:
            return ArticleUpdateDeleteSerializer

    def partial_update(self, request, *args, **kwargs):
        """
        게시글 부분 수정
        본인만 접근 가능
        사용자 전용
        """
        kwargs['partial'] = True

        return self.update(request, *args, **kwargs)