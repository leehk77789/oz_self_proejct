from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        # 유저 생성 메서드
        if not username:
            raise ValueError("username을 입력해주세요")
        user = self.model(username=username)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None):
        # 슈퍼유저 생성 메서드
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.save()
        return user

class User(AbstractBaseUser):
    # 사용자 모델 정의
    username = models.CharField(max_length=150, unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
