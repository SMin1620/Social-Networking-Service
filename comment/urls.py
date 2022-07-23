from django.urls import path

from comment.views import (
    CommentListrCreateViewSet,
)

comment_list = CommentListrCreateViewSet.as_view({
    'get': 'list'
})

comment_create = CommentListrCreateViewSet.as_view({
    'post': 'create'
})


urlpatterns = [
    path('', comment_list, name='comment list'),
    path('article/', comment_create, name='comment create')
]