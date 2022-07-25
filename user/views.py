from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from django.db import transaction, IntegrityError
from django.shortcuts import get_object_or_404

from user.serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserDetailSerializer,
    UserUpdateDeleteSerializer,
    UserFollowerSerializer,
)
from user.models import User, FollowRelation


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


class UserLoginViewSet(viewsets.GenericViewSet):
    """
    유저 로그인 뷰셋
    """
    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return LoginSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        """
        로그인 로직
        """
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            get_email = request.data.get('email')
            get_token = serializer.validated_data

            return Response({
                'message': f'로그인 되었습니다. 반갑습니다 {get_email}님',
                'token': get_token
            }, status=status.HTTP_200_OK)

        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class UserDetailUpdateDeleteViewSet(mixins.RetrieveModelMixin,
                                    mixins.UpdateModelMixin,
                                    mixins.DestroyModelMixin,
                                    viewsets.GenericViewSet):
    """
    유저 상세 조회
    유저 정보 수정
    유저 탈퇴
    사용자 전용
    """
    lookup_url_kwarg = 'user_id'

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserDetailSerializer
        elif self.request.method == 'POST':
            return UserFollowerSerializer
        else:
            return UserUpdateDeleteSerializer

    def partial_update(self, request, *args, **kwargs):
        """
        유저 정보 부분 수정
        사용자 전용
        """
        kwargs['partial'] = True

        return self.update(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    def follow(self, request, *args, **kwargs):
        user_id = kwargs['user_id']
        you = get_object_or_404(User, pk=user_id)
        me = request.user

        try:
            if you == me:
                raise IntegrityError

            if you.follow.filter(pk=me.id).exists():
                you.follow.remove(me.id)
                return Response({
                    'message': '언팔로우 했습니다.'
                }, status=status.HTTP_200_OK)
            else:
                you.follow.add(me.id)
                return Response({
                    'message': '팔로우 했습니다.'
                }, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response({
                'message': '자신한테는 팔로우를 할 수 없습니다.'
            }, status=status.HTTP_400_BAD_REQUEST)











