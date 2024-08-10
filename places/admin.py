from django.contrib import admin
from places.models import Place, Image
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableStackedInline
from adminsortable2.admin import SortableAdminBase


class PlaceImageStackedInline(SortableStackedInline):
    model = Image
    fields = ['img', 'get_preview']
    readonly_fields = ['get_preview']

    def get_preview(self, obj):
        
        return format_html(
           '<img src="{}" height="200">', obj.img.url
           )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        PlaceImageStackedInline
    ]
    search_fields = ['title']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('order', 'place')
    
