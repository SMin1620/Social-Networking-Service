from django.contrib import admin

from article.models import Article, ArticleLikedUser


# Register your models here.
admin.site.register(Article)
admin.site.register(ArticleLikedUser)
