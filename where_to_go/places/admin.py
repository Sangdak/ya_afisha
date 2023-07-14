from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image

from adminsortable2.admin import SortableTabularInline, SortableAdminBase


class ImageInline(SortableTabularInline):
    model = Image
    extra = 1
    readonly_fields = ('preview_img',)

    def preview_img(self, obj):
        return format_html(f'<img src="{obj.image.url}" height="200"/>')


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ['title']
    inlines = (ImageInline,)
