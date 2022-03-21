import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import strip_tags
from django.template.loader import render_to_string

class User(AbstractUser):

    """ 사용자 생성 모델 커스텀 """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    )

    LOGIN_GMAIL = "Gmail"
    LOGING_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_GMAIL, "Gmail"),
        (LOGING_KAKAO, "Kakao"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=150, default="", blank=True)
    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_GMAIL
    )
    
    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )
            send_mail(
                "회원가입 안전 절차 입니다.",
                # HTML to TEXT
                strip_tags(html_message),
                settings.DEFAULT_FROM_EMAIL,
                [self.email],
                fail_silently=False,
                html_message=html_message,
            )
            self.save()
        return