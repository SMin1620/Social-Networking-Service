from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django.db.models import Q, F


from article.models import (
    Article,
    ArticleLikedUser
)
from article.serializers import (
    ArticleListCreateSerializer,
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
            hashtag = self.request.GET.get('hashtags')  # 해시태그 입력
            search = self.request.GET.get('search')     # 검색 단어 입력

            hashtags = hashtag and hashtag.split(' ') and hashtag.split(',')    # 해시태그 필터

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
            queryset = Article.objects.filter(condition).distinct()
            return queryset

        else:
            return Article.objects.all()

    def get_serializer_class(self):
        return ArticleListCreateSerializer

    # 스웨거에서 query 파라미터를 입력받을 수 있기 위해 추가함. 없애도 됨
    param_hashtags = openapi.Parameter(
        'hashtags',
        openapi.IN_QUERY,
        description='filter',
        type=openapi.TYPE_STRING
        )

    # 스웨거에서 query 파라미터를 입력받을 수 있기 위해 추가함. 없애도 됨
    param_search = openapi.Parameter(
        'search',
        openapi.IN_QUERY,
        description='filter',
        type=openapi.TYPE_STRING
        )

    @swagger_auto_schema(manual_parameters=[param_hashtags, param_search])
    def list(self, request, *args, **kwargs):
        """
        게시글 목록 조회
        사용자 전용
        스웨거 데코레이터를 이용하기 위해서 선언함
        """
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)



