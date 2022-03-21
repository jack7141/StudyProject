from distutils.command.upload import upload
from email.mime import image
from django.db import models
from core.models import TimeStampedModel
from django.utils.safestring import mark_safe
from accounts.models import User

class Photo(TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="art_work")

    # 참조할 테이블 ART에서 리턴으로 받는값을 키로 값게됨
    art = models.ForeignKey("Art", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

    def get_thumbnail(self):
        return mark_safe(f'<img width="50px" src="{self.file.url}" />')

class Art(TimeStampedModel):

    """ Artist Model Definition """

    # 해당 아티스트가 여러장의 사진을 갖게됨
    artist = models.ForeignKey(
        "accounts.User", related_name="artist", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=140)
    description = models.TextField()

    def __str__(self):
        return str(self.artist)
