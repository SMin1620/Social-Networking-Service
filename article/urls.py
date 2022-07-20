from django.urls import path

from article.views import (
    ArticleListCreateViewSet,
)


article_list_create = ArticleListCreateViewSet.as_view({
    'get': 'list',
    'post': 'create'
})


urlpatterns = [
    path('', article_list_create, name='article list create'),
]