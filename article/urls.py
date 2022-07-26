from django.urls import path

from article.views import (
    ArticleListCreateViewSet,
    ArticleDetailUpdateDeleteViewSet,
    ArticleRestoreViewSet,
)


article_list_create = ArticleListCreateViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
article_detail_update_delete = ArticleDetailUpdateDeleteViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy',
})
article_like = ArticleDetailUpdateDeleteViewSet.as_view({
    'post': 'like'
})
article_delete_list = ArticleRestoreViewSet.as_view({
    'get': 'list'
})
article_delete_detail = ArticleRestoreViewSet.as_view({
    'get': 'retrieve',
    'patch': 'restore',
})


urlpatterns = [
    path('', article_list_create, name='article list create'),
    path('<int:article_id>/', article_detail_update_delete, name='article detail update delete'),
    path('<int:article_id>/like/', article_like, name='article like'),
    path('delete/', article_delete_list, name='article delete list'),
    path('delete/<int:article_id>/', article_delete_detail, name='article delete detail'),
]