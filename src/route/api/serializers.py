from rest_framework import serializers

from ..models import Route


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = (
            'climbingwall',
            'author',
            'name',
            'description',
            'grade',
            'marker',
            'rank',
            'active',
            'kind'
        )
