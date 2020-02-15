from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer


class UserSerializer(UserDetailsSerializer):
    description = serializers.CharField(source="profile.description")
    photo = serializers.CharField(source="profile.photo")

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('description', 'photo')

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        description = profile_data.get('description')
        photo = profile_data.get('photo')

        instance = super(UserSerializer, self).update(instance, validated_data)

        profile = instance.userprofile
        updated = False
        if profile_data:
            if description:
                updated = True
                profile.description = description
            if photo:
                updated = True
                profile.photo = photo
            if updated:
                profile.save()
        return instance
