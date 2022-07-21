from django.urls import path

from article.views import (
    ArticleListCreateViewSet,
    ArticleDetailUpdateDeleteViewSet
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


urlpatterns = [
    path('', article_list_create, name='article list create'),
    path('<int:article_id>/', article_detail_update_delete, name='article detail update delete'),
]