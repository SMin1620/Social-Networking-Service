from django.contrib.auth import get_user_model

from user.models import User

# 유저 더미데이터
def gen_master(apps, schema_editor):
    """
    author : 이승민
    explanation :
         - 유저 더미데이터
         - migration 파일에 적용시켜 migrate하면 유저를 자동으로 생성하게 해준다.
         - 슈퍼유저, 일반 유저 2~4
    """

    # 슈퍼 유저 생성
    User.objects.create_superuser(
        email="admin@email.com", username="admin", password="password"
    )

    # 일반 유저 생성
    for id in range(2, 5):
        email = f"user{id}@email.com"
        username = f"user{id}"
        password = "password"

        User.objects.create_user(email=email, username=username, password=password)