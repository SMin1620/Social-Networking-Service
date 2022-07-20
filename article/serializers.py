from rest_framework import serializers

from article.models import (
    Article,
    ArticleLikedUser
)


class ArticleListCreateSerializer(serializers.ModelSerializer):
    """
    게시글 조회
    게시글 생성
    사용자 전용
    """
    class Meta:
        model = Article
        fields = [
            'title',
            'hashtags',
            'user',
            'article_liked_user'
        ]
        write_only_fields = [
            'title',
            'content',
            'hashtags'
        ]


class ArticleFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'hashtags'
        ]