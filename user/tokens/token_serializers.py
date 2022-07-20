from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    토큰 커스텀 시리얼라이저
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['gender'] = user.gender
        token['username'] = user.username
        token['is_admin'] = user.is_admin
        token['is_active'] = user.is_active

        return token


class APIRefreshTokenSerializer(serializers.Serializer):
    """
    리프레시키를 이용한 엑세스키 재발급 시리얼라이저
    """
    refresh = serializers.CharField()
    pass


