import re

from django.db import models

from user.models import User
from tag.models import Tag


# Create your models here.
class Article(models.Model):
    title = models.CharField('제목', max_length=50)
    content = models.TextField('내용')
    hashtags = models.TextField('태그 내용')

    hits = models.PositiveIntegerField('조회수', default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    article_liked_user = models.ManyToManyField(User, through='article.ArticleLikedUser',
                                                related_name='liked_article')

    created_at = models.DateTimeField('등록 날짜', auto_now_add=True)
    updated_at = models.DateTimeField('수정 날짜', auto_now=True)

    # 사진도 추가해야함. (확장)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        old_tags = self.tags.all()
        new_tags = self.extract_tag_list()

        delete_tags: list[Tag] = []
        add_tags: list[Tag] = []

        for old_tag in old_tags:
            if not old_tag in new_tags:
                delete_tags.append(old_tag)

        for new_tag in new_tags:
            if not new_tag in old_tags:
                add_tags.append(new_tag)

        for delete_tag in delete_tags:
            self.tags.remove(delete_tag)

        for add_tag in add_tags:
            self.tags.add(add_tag)

    def extract_tag_list(self) -> list[Tag, ...]:
        tag_name_list = re.findall(r"#([a-zA-Z\dㄱ-힣]+)", self.hashtags)
        tag_list = []
        for tag_name in tag_name_list:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)
        return tag_list

    class Meta:
        db_table = 'article'
        ordering = ['-created_at']
        verbose_name = '게시글'
        verbose_name_plural = '게시글'

    def __str__(self):
        return f'{self.id} // title : {self.title}'


class ArticleLikedUser(models.Model):
    created_at = models.DateTimeField('등록 날짜', auto_now_add=True)
    updated_at = models.DateTimeField('수정 날짜', auto_now=True)

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'like'
        ordering = ['-created_at']
        verbose_name = '좋아요'
        verbose_name_plural = '좋아요'

    def __str__(self):
        return f'article : {self.article.title} // user : {self.user.username}'
