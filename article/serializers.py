from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _

from article.models import (
    Article,
    ArticleLikedUser
)
from user.serializers import UserSerializer
from comment.serializers import CommentSerializer


class ArticleListCreateSerializer(serializers.ModelSerializer):
    """
    게시글 조회
    게시글 생성
    사용자 전용
    """
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Article
        fields = [
            'user',
            'id',
            'title',
            'hashtags',
            'content',
        ]


class ArticleDetailSerializer(serializers.ModelSerializer):
    """
    게시글 상세 조회
    사용자 전용
    """
    like_count = serializers.SerializerMethodField(read_only=True)
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'content',
            'hashtags',
            'hits',
            'like_count',
            'created_at',
            'updated_at',
            'delete_date',
            'comments',
        ]

    def get_like_count(self, obj):
        return obj.article_liked_user.count()

    def get_comments(self, obj):
        serializer = CommentSerializer(obj.comments, many=True)
        return serializer.data


class ArticleUpdateDeleteSerializer(serializers.ModelSerializer):
    """
    게시글 수정
    게시글 삭제
    사용자 전용
    """
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'hashtags',
        ]

    def validate(self, attrs):
        if attrs['title'] is None:
            raise ValidationError(_('No title'))

        if attrs['content'] is None:
            raise ValidationError(_('No content'))

        if attrs['hashtags'] is None:
            raise ValidationError(_('No hashtags'))


class ArticleRestoreSerializer(serializers.ModelSerializer):
    """
    게시글 삭제 복구
    사용자 전용
    """
    user = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'hashtags',
            'user',
            'delete_date'
        ]
        read_only_fields = [
            'id',
            'title',
            'hashtags',
            'user',
            'delete_date'
        ]
