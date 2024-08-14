from adminsortable2.admin import SortableAdminBase, SortableStackedInline
from django.contrib import admin
from django.utils.html import format_html

from places.models import Image, Place


class PlaceImageStackedInline(SortableStackedInline):
    model = Image
    fields = ['img', 'get_preview']
    readonly_fields = ['get_preview']

    def get_preview(self, obj):

        return format_html(
           '<img src="{}" style="max-height: 200px;">', obj.img.url
           )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        PlaceImageStackedInline
    ]
    search_fields = ['title']


admin.site.register(Image)
