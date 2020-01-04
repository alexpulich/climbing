from rest_framework import serializers

from route.api.serializers import RouteShortSerializer
from ..models import TrainingDay, TrainingDayRoute


class TrainingDayRouteSerializer(serializers.ModelSerializer):
    route = RouteShortSerializer()

    class Meta:
        model = TrainingDayRoute
        fields = (
            'route',
            'attempts',
            'result'
        )


class TrainingDaySerializer(serializers.ModelSerializer):
    days = TrainingDayRouteSerializer(many=True, read_only=True)

    class Meta:
        model = TrainingDay
        fields = (
            'id',
            'date',
            'start_time',
            'end_time',
            'comments',
            'days'
        )
