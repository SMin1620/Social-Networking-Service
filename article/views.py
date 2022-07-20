from rest_framework import mixins, viewsets, status
from drf_yasg.utils import swagger_auto_schema

from django.db.models import Q, F
from rest_framework.response import Response

from article.models import (
    Article,
    ArticleLikedUser
)
from article.serializers import (
    ArticleListCreateSerializer,
    ArticleFilterSerializer,
)


# Create your views here.
class ArticleListCreateViewSet(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               viewsets.GenericViewSet):
    """
    게시글 조회 - 모든 사용자 접근 가능
    게시글 생성 - 인가된 사용자만 접근 가능
    사용자 전용 뷰셋
    """
    def get_queryset(self):
        hashtag = self.request.GET.get('hashtags', '')  # 해시태그 입력
        hashtags = hashtag and hashtag.split(' ') and hashtag.split(',')    # 해시태그 필터
        condition = Q()
        if hashtags:    # 입력받은 해시태그 파라미터가 있다면,
            # queryset = Article.objects.filter(tags__name__in=hashtags)
            condition.add(
                Q(tags__name__in=hashtags),
                Q.AND
            )
            queryset = Article.objects.filter(condition).distinct()
            return queryset
        else:
            return Article.objects.all()

    def get_serializer_class(self):
        return ArticleListCreateSerializer

    @swagger_auto_schema(query_serializer=ArticleFilterSerializer)  # 스웨거 쿼리 필터 적용, 없어도 됨
    def list(self, request, *args, **kwargs):
        """
        게시글 목록 조회
        사용자 전용
        스웨거 데코레이터를 이용하기 위해서 선언함
        """
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)



