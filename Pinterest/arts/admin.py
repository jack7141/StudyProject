from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models

@admin.register(models.Art)
class ArtAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("title", "description", "artist", "file")},
        ),
    )

    list_display = (
        "artist",
        'get_thumbnail',
    )



# @admin.register(models.Photo)
# class PhotoAdmin(admin.ModelAdmin):

#     """ Phot Admin Definition """

#     list_display = ("__str__", "get_thumbnail",)

