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
        'title',
        'get_thumbnail',
        "total_like",
    )

