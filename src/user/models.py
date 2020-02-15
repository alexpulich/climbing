from django.contrib.auth.models import User
from django.db import models

from common.models import TimeStampedModel


class Profile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(
        'Фотография',
        blank=True,
        upload_to='media/users/'
    )
    description = models.TextField(
        'О себе',
        blank=True
    )

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def __repr__(self):
        return f'<Profile {self.user}>'
