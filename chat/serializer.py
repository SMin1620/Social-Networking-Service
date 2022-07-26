from rest_framework import serializers

from chat.models import Room, Message
from user.models import User


class RoomSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Room
        fields = [
            'id',
            'title',
            'user',
            'created_at'
        ]


class MessageSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Message
        fields = [
            'id',
            'room',
            'sender',
            'content',
            'created_at'
        ]
        read_only_fields = [
            'id',
            'created_at'
        ]
        write_only_fields = [
            'content'
        ]