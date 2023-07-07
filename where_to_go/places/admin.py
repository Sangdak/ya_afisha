from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ('preview_img',)

    def preview_img(self, obj):
        return format_html(f'<img src="{obj.get_url()}" height="200"/>')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (ImageInline,)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['order', 'place']
