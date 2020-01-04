from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from common.models import TimeStampedModel
from climbingwall.models import Climbingwall


class PhoneNumber(TimeStampedModel):
    phone = PhoneNumberField(blank=True)
    climbingwall = models.ForeignKey(
        Climbingwall,
        on_delete=models.CASCADE,
        related_name='phones'
    )

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

    def __str__(self):
        return str(self.phone)

    def __repr__(self):
        return f'<Phone {self.phone}>'


class Email(TimeStampedModel):
    email = models.EmailField(blank=True)
    climbingwall = models.ForeignKey(
        Climbingwall,
        on_delete=models.CASCADE,
        related_name='emails'
    )

    class Meta:
        verbose_name = 'E-mail'
        verbose_name_plural = 'E-mails'

    def __str__(self):
        return self.email

    def __repr__(self):
        return f'<Email {self.email}>'
