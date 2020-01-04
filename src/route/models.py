from django.contrib.auth.models import User
from django.db import models

from common.models import ClimbingKind, TimeStampedModel
from climbingwall.models import Climbingwall


class Route(TimeStampedModel):
    GRADE_CHOICES = (
        ('5a', '5a'),
        ('5a+', '5a+'),
        ('5b', '5b'),
        ('5b+', '5b+'),
        ('5c', '5c'),
        ('5c+', '5c+'),
        ('6a', '6a'),
        ('6a+', '6a+'),
        ('6b', '6b'),
        ('6b+', '6b+'),
        ('6c', '6c'),
        ('6c+', '6c+'),
        ('7a', '7a'),
        ('7a+', '7a+'),
        ('7b', '7b'),
        ('7b+', '7b+'),
        ('7c', '7c'),
        ('7c+', '7c+'),
        ('8a', '8a'),
        ('8a+', '8a+'),
        ('8b', '8b'),
        ('8b+', '8b+'),
        ('8c', '8c'),
        ('8c+', '8c+'),
        ('9a', '9a'),
        ('9a+', '9a+'),
        ('9b', '9b'),
        ('9b+', '9b+'),
        ('9c', '9c'),
        ('9c+', '9c+'),
    )

    climbingwall = models.ForeignKey(
        Climbingwall,
        related_name='routes',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        related_name='routes',
        on_delete=models.CASCADE
    )
    name = models.CharField('Название', max_length=100)
    description = models.CharField(
        'Описание',
        max_length=255,
        blank=True
    )
    grade = models.CharField(
        'Категория',
        max_length=3,
        choices=GRADE_CHOICES
    )
    marker = models.CharField('Метка', max_length=100)

    rank = models.IntegerField('Рейтинг', default=0)
    active = models.BooleanField('Активная', default=True)
    kind = models.ForeignKey(
        ClimbingKind,
        related_name='routes',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Трасса'
        verbose_name_plural = 'Трассы'

    def __str__(self):
        return f'{self.name} ({self.grade})'

    def __repr__(self):
        return f'<Route {self.name}>'


class RoutePhoto(TimeStampedModel):
    photo = models.ImageField('Фотография', upload_to='media/routes/')
    route = models.ForeignKey(
        Route,
        related_name='photos',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Фотография трассы'
        verbose_name_plural = 'Фотографии трассы'

    def __str__(self):
        return f'Фотография трассы {self.route}'

    def __repr__(self):
        return f'<RoutePhoto {self.pk}>'
