from distutils.command.upload import upload
from email.mime import image
from django.db import models
from core.models import TimeStampedModel

from accounts.models import User

class Art(TimeStampedModel):
    """
    * 아트 모델 
    """
    artist = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='art', null=True)

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='art', null=False)
    desciption = models.TextField(null=True)


