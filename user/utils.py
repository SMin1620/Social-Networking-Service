from datetime import timezone

from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from user.models import User


def validate_password12(password1, password2):
    """
    author : 이승민
    :param password1: 첫 번째 비밀번호
    :param password2: 두 번째 비밀번호
    :return: password1
    error :
        - password1 validate
        - password1, 2 require
        - password1 == password2
    explanation :
        - 회원가입 시 password1, password2를 입력 후 일치하는 비교
        - 영문자 대소문자, 숫자, 특수문자(리스트)만 허용
        - 영어 대소문자 필수
        - 특수문자 필수
        - 글자수 제한
    """
    validate_condition = [

        lambda s: all(
            x.islower()
            or x.isupper()
            or x.isdigit()
            or (x in ["!", "@", "#", "$", "%", "^", "&", "*", "_"])
            for x in s
        ),  ## 영문자 대소문자, 숫자, 특수문자(리스트)만 허용
        lambda s: any(x.islower() or x.isupper() for x in s),  ## 영어 대소문자 필수
        lambda s: any(
            (x in ["!", "@", "#", "$", "%", "^", "&", "*", "_"]) for x in s
        ),  ## 특수문자 필수
        lambda s: len(s) == len(s.replace(" ", "")),
        lambda s: len(s) >= 6,
        lambda s: len(s) <= 20,
    ]

    for validator in validate_condition:
        if not validator(password1):
            raise serializers.ValidationError(_("password ValidationError"))

    if not password1 or not password2:
        raise serializers.ValidationError(_("need two password fields"))
    if password1 != password2:
        raise serializers.ValidationError(_("password fields didn't match!"))

    return password1


def get_user_login(user: User):
    """
    해당 유저의 마지막 로그인 시간 업데이트
    """
    user.las_login = timezone.now()
    user.save()

    return user
