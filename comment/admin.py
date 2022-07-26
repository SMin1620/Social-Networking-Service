from django.contrib import admin

from comment.models import Comment, ReComment

# Register your models here.
admin.site.register(Comment)
admin.site.register(ReComment)
