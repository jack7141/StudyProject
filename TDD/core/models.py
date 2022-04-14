from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# [참고 자료]
# https://www.coninggu.com/m/8

class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        """
        * BaseUserManager의 create_user 메소드 오버라이드
        :param email:
        :param password:
        :param extra_fileds:
        :return:
        """
        if not email:
            return ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """
    * 유저의 이름을 이메일로 대체합니다.
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'