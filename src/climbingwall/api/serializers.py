from rest_framework import serializers

from common.serializers import ClimbingKindSerializer
from contacts.serializers import EmailSerializer, PhoneNumberSerializer
from timetable.serializers import TimetableSerializer
from ..models import Climbingwall


class ClimbingwallSerializer(serializers.ModelSerializer):
    kinds = ClimbingKindSerializer(many=True, read_only=True)
    phones = PhoneNumberSerializer(many=True, read_only=True)
    emails = EmailSerializer(many=True, read_only=True)
    timetable = TimetableSerializer(many=True, read_only=True)

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
