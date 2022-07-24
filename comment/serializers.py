from rest_framework import serializers

from comment.models import Comment, ReComment


class CommentSerializer(serializers.ModelSerializer):
    """
    댓글 시리얼라이저
    """
    article = serializers.ReadOnlyField(source='article.id')
    user = serializers.ReadOnlyField(source='user.username')
    re_comments = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'article',
            'user',
            'content',
            'created_at',
            're_comments',
        ]

    def get_re_comments(self, obj):
        serializer = ReCommentSerializer(obj.re_comments, many=True)
        return serializer.data


class CommentCreateSerializer(serializers.ModelSerializer):
    """
    댓글 생성 시리얼라이저
    """
    user = serializers.ReadOnlyField(source='user.email')
    article = serializers.ReadOnlyField(source='article.title')

    class Meta:
        model = Comment
        fields = [
            'content',
            'user',
            'article',
        ]


class CommentUpdateDeleteSerializer(serializers.ModelSerializer):
    """
    댓글 수정
    댓글 삭제
    시리얼라이저
    """
    class Meta:
        model = Comment
        fields = [
            'content'
        ]


class ReCommentSerializer(serializers.ModelSerializer):
    """
    대댓글 시리얼라이저
    """
    user = serializers.ReadOnlyField(source='user.username')
    comment = serializers.ReadOnlyField(source='comment.id')

    class Meta:
        model = ReComment
        fields = [
            'id',
            'content',
            'created_at',
            'user',
            'comment',
        ]


class ReCommentListCreateSerializer(serializers.ModelSerializer):
    """
    대댓글 전체 조회
    대댓글 생성
    시리얼라이저
    사용자 전용
    """
    user = serializers.ReadOnlyField(source='user.username')
    comment = serializers.ReadOnlyField(source='comment.id')

    class Meta:
        model = ReComment
        fields = [
            'content',
            'user',
            'comment',
        ]
