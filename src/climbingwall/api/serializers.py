from rest_framework import serializers

from common.api.serializers import ClimbingKindSerializer
from contacts.api.serializers import EmailSerializer, PhoneNumberSerializer
from social_networks.api.serializers import SocialNetworkLinkSerializer
from timetable.api.serializers import TimetableSerializer
from ..models import Climbingwall, ClimbingwallPhoto


class ClimbingwallPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClimbingwallPhoto
        fields = ('photo',)


class ClimbingwallSerializer(serializers.ModelSerializer):
    kinds = ClimbingKindSerializer(many=True, read_only=True)
    phones = PhoneNumberSerializer(many=True, read_only=True)
    emails = EmailSerializer(many=True, read_only=True)
    timetable = TimetableSerializer(many=True, read_only=True)
    photos = ClimbingwallPhotoSerializer(many=True, read_only=True)
    links = SocialNetworkLinkSerializer(many=True, read_only=True)

    class Meta:
        model = Climbingwall
        fields = (
            'id',
            'name',
            'description',
            'logo',
            'kinds',
            'city',
            'address',
            'url',
            'photos',
            'phones',
            'emails',
            'links',
            'timetable'
        )
