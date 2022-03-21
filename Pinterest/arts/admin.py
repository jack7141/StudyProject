from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models

@admin.register(models.Art)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("title", "description", "artist")},
        ),
    )

    list_display = (
        "artist",
        "count_photos",
    )

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Phot Admin Definition """

    list_display = ("__str__", "get_thumbnail")

