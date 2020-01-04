from rest_framework import serializers

from ..models import Route


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = (
            'id',
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


class RouteShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = (
            'id',
            'name',
            'grade',
        )
