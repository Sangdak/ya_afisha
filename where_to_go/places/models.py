from django.db import models

from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='Название',
    )
    description_short = models.TextField(
        blank=True,
        verbose_name='Краткое описание',
    )
    description_long = HTMLField(
        blank=True,
        verbose_name='Развёрнутое описание'
    )
    lng = models.FloatField(
        verbose_name='Координаты: долгота'
    )
    lat = models.FloatField(
        verbose_name='Координаты: широта'
    )

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Место',
    )
    image = models.ImageField(
        verbose_name='Изображение',
    )
    order = models.PositiveIntegerField(
        default=1,
        verbose_name='Порядковый номер',
    )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['order']

    def __str__(self):
        return f'{self.order} изображение {self.place.title}'
