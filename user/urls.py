from django.urls import path

from user.views import (
    UserCreateViewSet,
    UserLoginViewSet,
)


user_register = UserCreateViewSet.as_view({
    'post': 'register'
})
user_login = UserLoginViewSet.as_view({
    'post': 'login'
})


urlpatterns = [
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
]