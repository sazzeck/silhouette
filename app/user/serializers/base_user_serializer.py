from rest_framework import serializers

from user.models import BaseUser


class BaseUserListSerializer(serializers.ModelSerializer):
    id = serializers.CharField()

    class Meta:
        model = BaseUser
        read_only_fields = (
            "is_online",
        )

        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "is_online",
        )


class BaseUserDetailSerializer(serializers.ModelSerializer):
    id = serializers.CharField()

    class Meta:
        model = BaseUser
        read_only_fields = (
            "password",
            "last_login",
            "date_joined",
            "is_online",
        )

        fields = (
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "last_login",
            "date_joined",
            "is_online",
        )
