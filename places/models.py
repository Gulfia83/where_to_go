from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name='Название компании')
    description_short = models.TextField(verbose_name='Краткое описание',
                                         blank=True,
                                         null=True)
    description_long = models.TextField(verbose_name='Полное описание',
                                        blank=True,
                                        null=True)
    lat = models.FloatField(verbose_name='Широта',
                            null=True)
    lon = models.FloatField(verbose_name='Долгота',
                            null=True)
    
    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place,
                              on_delete=models.CASCADE,
                             verbose_name='Место',
                             related_name='images')
    img = models.ImageField(verbose_name='Фото')
    order = models.PositiveIntegerField(verbose_name='Порядковый номер',
                                        default=0)
    
    def __str__(self):
        return self.place.title