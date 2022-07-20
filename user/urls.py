from django.urls import path

from user.views import (
    UserCreateViewSet,
    UserLoginViewSet,
    UserDetailUpdateDeleteViewSet,
)


user_register = UserCreateViewSet.as_view({
    'post': 'register'
})
user_login = UserLoginViewSet.as_view({
    'post': 'login'
})
user_detail = UserDetailUpdateDeleteViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('<int:user_id>/', user_detail, name='user detail')
]