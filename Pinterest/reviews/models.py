from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    review = models.TextField(null=False)

    user = models.ForeignKey("accounts.User", related_name="reviews", on_delete=models.SET_NULL,null=True)

    art = models.ForeignKey("arts.Art", related_name="reviews", on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.user} - {self.art}"

