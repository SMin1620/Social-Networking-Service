from rest_framework import serializers

from comment.models import Comment, ReComment


class CommentSerializer(serializers.ModelSerializer):
    """
    댓글 시리얼라이저
    """
    article = serializers.ReadOnlyField(source='article.id')
    user = serializers.ReadOnlyField(source='user.email')
    recomment = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'article',
            'user',
            'content',
            'recomment',
            'created_at',
            'updated_at',
        ]

    def get_recomment(self, instance):
        serializer = self.__class__(instance.recomment, many=True)
        serializer.bind('', self)
        return serializer.data


class CommentCreateSerializer(serializers.ModelSerializer):
    """
    댓글 생서 시리얼라이저
    """
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Comment
        fields = [
            'content',
            'article',
            'user',
        ]