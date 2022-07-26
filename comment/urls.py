from django.urls import path

from comment.views import (
    CommentListrCreateViewSet,
    CommentUpdateDeleteViewSet,
    ReCommentListCreateViewSet,
    ReCommentUpdateDeleteViewSet
)

comment_list = CommentListrCreateViewSet.as_view({
    'get': 'list',
})

comment_create = CommentListrCreateViewSet.as_view({
    'post': 'create'
})

comment_update_delete = CommentUpdateDeleteViewSet.as_view({
    'patch': 'partial_update',
    'delete': 'destroy',
})

re_comment_list_create = ReCommentListCreateViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

re_comment_update_delete = ReCommentUpdateDeleteViewSet.as_view({
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('', comment_list, name='comment list'),
    path('<article_id>/comment/', comment_create, name='comment create'),
    path('<comment_id>/', comment_update_delete, name='comment update delete'),
    path('<comment_id>/recomment/', re_comment_list_create, name='recomment list create'),
    path('recomment/<recomment_id>/', re_comment_update_delete, name='recomment update delete'),
]