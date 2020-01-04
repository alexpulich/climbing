from django.db import models

from common.models import ClimbingKind, TimeStampedModel


class Climbingwall(TimeStampedModel):
    name = models.CharField('Название', max_length=255, unique=True)
    description = models.TextField('Описание', blank=True)
    logo = models.ImageField('Логотип', blank=True)
    kinds = models.ManyToManyField(ClimbingKind, related_name='climbingwalls')
    city = models.CharField('Город', max_length=100, blank=True)
    address = models.CharField('Адрес', max_length=255, blank=True)
    url = models.URLField('Веб-сайт', blank=True)

    class Meta:
        verbose_name = 'Скалодром'
        verbose_name_plural = 'Скалодромы'

    def __str__(self):
        return f'Скалодром "{self.name}"'

    def __repr__(self):
        return f'<ClimbingWall {self.pk}>'


class ClimbingwallPhoto(TimeStampedModel):
    photo = models.ImageField('Фото', blank=True, upload_to='media/climbingwalls/')
    climbingwall = models.ForeignKey(
        Climbingwall,
        related_name='photos',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Фотография скалодрома'
        verbose_name_plural = 'Фотографии скалодрома'

    def __str__(self):
        return f'Фотография скалодрома {self.climbingwall}'

    def __repr__(self):
        return f'<ClimbingWallPhoto {self.pk}>'
