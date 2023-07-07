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
    coordinates_lng = models.FloatField(
        verbose_name='Координаты: долгота'
    )
    coordinates_lat = models.FloatField(
        verbose_name='Координаты: широта'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


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
        verbose_name='Порядковый номер',
    )

    def get_url(self):
        return self.image.url

    def __str__(self):
        return f'{self.order} изображение {self.place.title}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
