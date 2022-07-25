from rest_framework import mixins, viewsets, status

from django.db import transaction
from django.shortcuts import get_object_or_404, render

from chat.models import Room, Message
from chat.serializer import (
    RoomSerializer,
    MessageSerializer
)

from SNS.drf.permissions import IsOwnerOrReadOnly


# Create your views here.
class RoomListCreateViewSet(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    """
    채팅방 전체 조회
    채팅방 생성
    뷰셋
    """
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Room.objects.all()

    def get_serializer_class(self):
        return RoomSerializer

    @transaction.atomic()
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

