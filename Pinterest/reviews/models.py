from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    review = models.TextField()
    user = models.ForeignKey(
        "accounts.User", related_name="reviews", on_delete=models.CASCADE
    )
    art = models.ForeignKey(
        "arts.Art", related_name="reviews", on_delete=models.CASCADE
    )
    
    is_like = models.BooleanField(null=True, default=False)
    
    def __str__(self):
        return f"{self.review} - {self.art}"

