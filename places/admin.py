from django.contrib import admin
from places.models import Place, Image


class PlaceImageInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PlaceImageInline
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('order', 'place')
    
