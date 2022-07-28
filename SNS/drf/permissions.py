from rest_framework.permissions import BasePermission, SAFE_METHODS

from django.contrib.auth import get_user_model

from article.models import Article


class IsOwnerOrReadOnly(BasePermission):
    # 작성자만 접근, 작성자가 아니면 Read만 가능
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.is_staff():
                return True
            # 값을 바꾸지 않는 안전한 method
            elif request.method in SAFE_METHODS:
                return True
            elif hasattr(obj, 'user'):
                return obj.user.id == request.user.id
            elif obj.__class__ == get_user_model():
                return obj.id == request.user.id
            return False
        else:
            # 인가되지 않은 사용자도 게시글 확인 가능
            if request.method in SAFE_METHODS:
                return True
            return False
