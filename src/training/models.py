from django.contrib.auth.models import User
from django.db import models

from common.models import TimeStampedModel
from route.models import Route


class TrainingDay(TimeStampedModel):
    comments = models.TextField('Комментарии')
    date = models.DateField('Дата')
    start_time = models.TimeField('Время начала')
    end_time = models.TimeField('Время конца')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='days'
    )

    class Meta:
        verbose_name = 'Тренировочный день'
        verbose_name_plural = 'Тренировочные дни'

    def __str__(self):
        return str(self.date)

    def __repr__(self):
        return f'<TrainingDay {self.date}>'


class TrainingDayRoute(TimeStampedModel):
    day = models.ForeignKey(
        TrainingDay,
        related_name='days',
        on_delete=models.CASCADE
    )
    route = models.ForeignKey(
        Route,
        on_delete=models.CASCADE,
        related_name='routes'
    )
    attempts = models.SmallIntegerField()
    result = models.TextField()

    class Meta:
        verbose_name = 'Трасса с тренировки'
        verbose_name_plural = 'Трассы с тренировки'

    def __str__(self):
        return f'{self.day} {self.route}'

    def __repr__(self):
        return f'<TrainingDayRoute {self.day} {self.route}>'
