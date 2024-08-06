from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name='Название места')
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
