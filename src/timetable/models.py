from django.db import models

from common.models import TimeStampedModel
from climbingwall.models import Climbingwall


class Timetable(TimeStampedModel):
    DAYS = (
        ('Пн', 'Понедельник'),
        ('Вт', 'Вторник'),
        ('Ср', 'Среда'),
        ('Чт', 'Четверг'),
        ('Пт', 'Пятница'),
        ('Сб', 'Суббота'),
        ('Вс', 'Восскресенье'),
    )

    day = models.CharField('День недели', max_length=2, choices=DAYS)
    open_at = models.TimeField('Время открытия')
    close_at = models.TimeField('Время закрытия')
    climbingwall = models.ForeignKey(
        Climbingwall,
        on_delete=models.CASCADE,
        related_name='timetable'
    )

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
        unique_together = ['day', 'climbingwall']

    def __str__(self):
        return self.day

    def __repr__(self):
        return f'<Timetable {self.day}>'
