from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        abstract = True


class ClimbingKind(models.Model):
    name = models.CharField('Название', max_length=20)

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<ClimbingKind {self.name}>'
