from django.contrib.auth import authenticate
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from user.models import User
from user.utils import validate_password12


class RegisterSerializer(serializers.Serializer):
    """
    author : 이승민
    explanation :
        - 회원가입 시리얼라이저
        - email, password1, password2, nickname의 validate 확인
    error :
         - validate_email : 이메일 입력 확인, 이메일 형식 확인, 이메일 중복 확인
         - validate_nickname : 닉네임 입력 확인, 닉네임 중복 확인
    """
    email = serializers.EmailField(max_length=100, write_only=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    username = serializers.CharField(max_length=100, write_only=True)

    def validate_email(self, email):
        """
        이메일 유효성 검사
        """
        if not email:   # 이메일을 입력하지 않았을 때, ,
            raise serializers.ValidationError(_("email field not allowed empty"))

        get_email = User.objects.filter(email__iexact=email)
        if get_email.count() > 0:   # 이메일이 이미 가입되어있다면,
            raise serializers.ValidationError(_("email is already registered"))

        return email

    def validate_username(self, username):
        """
        사용자 이름 유효성 검사
        """
        if not username:    # 이름을 입력하지 않았 때,
            raise serializers.ValidationError(_("username field not allowed empty"))

        return username

    def validate(self, data):
        """
        유효성 검사가 완료된 데이터
        """
        data["password1"] = validate_password12(data["password1"], data["password2"])
        data["email"] = self.validate_email(data["email"])
        data["username"] = self.validate_username(data["username"])

        return data

    def create(self, validate_data):
        """
        사용자 생성
        """
        user = User.objects.create_user(
            email=validate_data["email"],
            password=validate_data["password1"],
            username=validate_data["username"],
        )

        return user






