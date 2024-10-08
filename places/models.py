from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=255,
                             unique=True,
                             verbose_name='Название')
    short_description = models.TextField(verbose_name='Краткое описание',
                                         blank=True)
    long_description = HTMLField(verbose_name='Полное описание',
                                 blank=True)
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place,
                              on_delete=models.CASCADE,
                              verbose_name='Место',
                              related_name='images')
    img = models.ImageField(verbose_name='Фото')
    order = models.PositiveIntegerField(verbose_name='Порядковый номер',
                                        default=0,
                                        db_index=True)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return self.place.title
