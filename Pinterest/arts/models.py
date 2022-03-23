from distutils.command.upload import upload
from email.mime import image
from django.db import models
from core.models import TimeStampedModel
from django.utils.safestring import mark_safe

class Art(TimeStampedModel):

    """ Artist Model Definition """

    # 해당 아티스트가 여러장의 사진을 갖게됨
    artist = models.ForeignKey(
        "accounts.User", related_name="artist", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=140)
    description = models.TextField()
    file = models.ImageField(upload_to="art_work")
    
    like_users = models.ManyToManyField("accounts.User", related_name="like_posts", blank=True)
    def __str__(self):
        return str(self.title)


    def get_thumbnail(self):
        return mark_safe(f'<img width="50px" src="{self.file.url}" />')

    def total_like(self):
        # 좋아요 갯수 카운트
        all_likes = self.reviews.all()
        count_like = 0
        for all_like in all_likes:
            if all_like.is_like is True:
                count_like+=1
        return count_like

    def get_users(self):
        return "\n".join([p.like_users for p in self.like_users.all()])