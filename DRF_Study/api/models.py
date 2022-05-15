from django.db import models
# Create your models here.

class Reviews(models.Model):
    account_alias = models.CharField(primary_key=True,  max_length=128)
