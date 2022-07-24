from rest_framework import mixins, viewsets, status
from rest_framework.permissions import (
    IsAdminUser,
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from django.db import transaction
from django.shortcuts import get_object_or_404

from comment.models import Comment, ReComment
from comment.serializers import (
    CommentSerializer,
    CommentCreateSerializer,
    CommentUpdateDeleteSerializer,
    ReCommentSerializer,
    ReCommentListCreateSerializer,
)
from SNS.drf.permissions import IsOwnerOrReadOnly
from article.models import Article


# Create your views here.
class CommentListrCreateViewSet(mixins.ListModelMixin,
                                mixins.CreateModelMixin,
                                viewsets.GenericViewSet):
    """
    댓글 전체 조회
    댓글 생성
    사용자 전용
    """
    lookup_url_kwarg = 'article_id'
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Comment.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CommentSerializer
        else:
            return CommentCreateSerializer

    @transaction.atomic()
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        article_id = self.kwargs['article_id']
        article = get_object_or_404(Article, pk=article_id)
        serializer.save(user=self.request.user, article=article)


class CommentUpdateDeleteViewSet(mixins.UpdateModelMixin,
                                 mixins.DestroyModelMixin,
                                 viewsets.GenericViewSet):
    """
    댓글 수정
    댓글 삭제
    사용자 전용
    """
    lookup_url_kwarg = 'comment_id'
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Comment.objects.all()

    def get_serializer_class(self):
        return CommentUpdateDeleteSerializer

    def partial_update(self, request, *args, **kwargs):
        """
        댓글 부분 수정
        본인만 접근 가능
        사용자 전용
        """
        kwargs['partial'] = True

        return self.update(request, *args, **kwargs)


class ReCommentListCreateViewSet(mixins.ListModelMixin,
                                 mixins.RetrieveModelMixin,
                                 mixins.CreateModelMixin,
                                 viewsets.GenericViewSet):
    """
    대댓글 전체 조회
    대댓글 생성
    뷰셋
    사용자 전용
    """
    lookup_url_kwarg = 'comment_id'
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return ReComment.objects.all()

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return ReCommentSerializer
    #     else:
    #         return ReCommentListCreateSerializer
    def get_serializer_class(self):
        return ReCommentSerializer

    @transaction.atomic()
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

