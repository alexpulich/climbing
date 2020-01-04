from rest_framework import serializers

from .models import Email, PhoneNumber


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ('phone',)


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ('email',)
