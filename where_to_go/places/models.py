from django.db import models


class Place(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='Название',
    )
    description_short = models.CharField(
        max_length=255,
        verbose_name='Краткое описание',
    )
    description_long = models.TextField(
        verbose_name='Развёрнутое описание'
    )
    сoordinates_lng = models.FloatField()
    сoordinates_lat = models.FloatField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
