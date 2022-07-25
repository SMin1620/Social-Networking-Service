from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, username, password, **extra_fields):

        if not email:
            raise ValueError("이메일은 필수 항목입니다.")
        if not password:
            raise ValueError("비밀번호는 필수 항목입니다.")
        if not username:
            raise ValueError("이름은 필수 항목 입니다.")

        user = self.model(
            email=UserManager.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, username, **extra_fields):

        user = self.model(
            email=email,
            username=username,
        )
        user.set_password(password)
        user.full_clean()

        user.is_admin = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = 'M', '남성'
        FEMALE = 'F', '여성'

    first_name = None
    last_name = None
    date_joined = None

    email = models.EmailField('이메일', max_length=255, unique=True)
    username = models.CharField('이름', max_length=50)
    gender = models.CharField('성별', max_length=1, blank=True, choices=GenderChoices.choices)

    follow = models.ManyToManyField('self', symmetrical=False, through='user.FollowRelation',
                                    related_name='follow_user')

    reg_date = models.DateTimeField('생성 날짜', auto_now_add=True)
    update_date = models.DateTimeField('수정 날짜', auto_now=True)

    last_login = models.DateTimeField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'user'
        ordering = ['-id']
        verbose_name = '회원'
        verbose_name_plural = '회원들'

    def natural_key(self):
        return self.email

    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return f'{self.id}, {self.email}, {self.username}'


class FollowRelation(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower', default=0)
    followee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followee', default=0)

    class Meta:
        db_table = 'follow'

    def __str__(self):
        return f'Follower : {self.follower.email} // Followee : {self.followee.email}'
