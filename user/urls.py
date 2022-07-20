from django.urls import path

from user.views import (
    UserCreateViewSet,
)


user_register = UserCreateViewSet.as_view({
    'post': 'register'
})


urlpatterns = [
    path('register/', user_register, name='register'),
]