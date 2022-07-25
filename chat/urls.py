from django.urls import path

from chat.views import (
    RoomListCreateViewSet,
)


room_create = RoomListCreateViewSet.as_view({
    'get': 'list',
    'post': 'create'
})


urlpatterns = [
    path('room/', room_create, name='room create'),
]