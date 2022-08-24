from rest_framework import serializers

from user.models import BaseUser


class BaseUserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = BaseUser
        fields = (
            "id",
            "username",
            "date_joined",
            "is_online",
        )


class BaseUserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = BaseUser
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "last_login",
            "date_joined",
            "is_staff",
            "is_active",
            "is_online",
        )
