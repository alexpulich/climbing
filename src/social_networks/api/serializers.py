from rest_framework import serializers

from ..models import SocialNetworkLink


class SocialNetworkLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetworkLink
        fields = ('network', 'url')
