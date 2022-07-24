from django.db import models

from user.models import User
from article.models import Article


# Create your models here.
class Comment(models.Model):
    content = models.TextField('댓글 내용')

    created_at = models.DateTimeField('생성 날짜', auto_now_add=True)
    updated_at = models.DateTimeField('수정 날짜', auto_now=True)

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True)

    class Meta:
        db_table = 'comment'
        ordering = ['-id']
        verbose_name = '댓글'
        verbose_name_plural = '댓글들'

    def __str__(self):
        return f'{self.id} // Article : {self.article}, User : {self.user}'


class ReComment(models.Model):
    content = models.TextField('대댓글 내용')

    created_at = models.DateTimeField('생성 날짜', auto_now_add=True)
    updated_at = models.DateTimeField('수정 날짜', auto_now=True)

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.DO_NOTHING, blank=True, related_name='re_comments')

    class Meta:
        db_table = 'recomment'
        ordering = ['-id']
        verbose_name = '대댓글'
        verbose_name_plural = '대댓글들'

    def __str__(self):
        return f'{self.id} // Article : {self.article}, User : {self.user} // Comment : {self.comment}'




