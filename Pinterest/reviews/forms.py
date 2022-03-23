from django import forms

from . import models
class review_form(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ("review",)

