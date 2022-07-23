from rest_framework import mixins, viewsets, status
from rest_framework.permissions import (
    IsAdminUser,
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from django.db import transaction

from comment.models import Comment, ReComment
from comment.serializers import (
    CommentSerializer,
    CommentCreateSerializer
)
from SNS.drf.permissions import IsOwnerArticle


# Create your views here.
class CommentListrCreateViewSet(mixins.ListModelMixin,
                                mixins.CreateModelMixin,
                                viewsets.GenericViewSet):
    """
    댓글 생성
    사용자 전용
    """
    permission_classes = (IsAuthenticated, )

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
        serializer.save(user=self.request.user)

