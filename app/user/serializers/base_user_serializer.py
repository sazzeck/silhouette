from rest_framework import serializers

from user.models import BaseUser


class BaseUserListSerializer(serializers.ModelSerializer):
    id = serializers.CharField()

    class Meta:
        model = BaseUser

        fields = (
            "id",
            "username",
            "password",
        )


class BaseUserDetailSerializer(serializers.ModelSerializer):
    id = serializers.CharField()

    class Meta:
        model = BaseUser
        read_only_fields = (
            "last_login",
            "date_joined",
        )

        fields = (
            "id",
            "username",
            "password",
            "last_login",
            "date_joined",
        )
