from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ 사용자 생성 모델 커스텀 """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    )


    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)