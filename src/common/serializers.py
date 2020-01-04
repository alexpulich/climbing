from rest_framework import serializers

from .models import ClimbingKind


class ClimbingKindSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClimbingKind
        fields = [
            'id',
            'name',
        ]
