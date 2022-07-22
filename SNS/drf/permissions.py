from rest_framework.permissions import BasePermission

from article.models import Article


class IsOwnerArticle(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.id == obj.id:
                return True
            return False
        else:
            return False