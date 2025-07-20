from django.contrib import admin
from django.utils.html import format_html

from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['file', 'id', 'preview']

    def preview(self, obj):
        if obj.file:
            return format_html('<img src="{}" width="100" />', obj.file.url)
        return "-"
    preview.short_description = 'Preview'
