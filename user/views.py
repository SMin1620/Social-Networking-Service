from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from django.db import transaction

from user.serializers import (
    RegisterSerializer,
)
from user.models import User


# Create your views here.
class UserCreateViewSet(viewsets.GenericViewSet):
    """
    회원가입 뷰셋
    """
    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return RegisterSerializer

    @transaction.atomic
    @action(detail=False, methods=['post'])
    def register(self, request):
        """
        회원가입 로직
        """
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):   # 유효성 검사 에러 발생
            return Response({
                    'message': 'Request Body Error'
                }, status=status.HTTP_409_CONFLICT)

        serializer.save()

        return Response({
                'message': '회원가입이 되었습니다.'
            }, status=status.HTTP_200_OK)







