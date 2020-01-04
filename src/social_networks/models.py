from django.db import models

from common.models import TimeStampedModel
from climbingwall.models import Climbingwall


class SocialNetwork(TimeStampedModel):
    name = models.CharField(max_length=20)
    short_name = models.CharField(max_length=10)
    base_url = models.URLField()

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<SocialNetwork {self.name}>'


class SocialNetworkLink(TimeStampedModel):
    url = models.URLField()
    network = models.ForeignKey(
        SocialNetwork,
        on_delete=models.CASCADE,
        related_name='links'
    )
    climbingwall = models.ForeignKey(
        Climbingwall,
        on_delete=models.CASCADE,
        related_name='links'
    )

    class Meta:
        verbose_name = 'Ссылка социальной сети'
        verbose_name_plural = 'Ссылки социальной сети'

    def __str__(self):
        return self.url

    def __repr__(self):
        return f'<SocialNetworkLink {self.url}>'
