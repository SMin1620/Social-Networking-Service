from django.contrib import admin

from article.models import Article, ArticleLikedUser
from SNS.models import SoftDeleteModel, SoftDeleteManager


# Register your models here.
admin.site.register(Article)
admin.site.register(ArticleLikedUser)
