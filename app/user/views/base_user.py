from rest_framework import viewsets, mixins

from user.models import BaseUser
from user.serializers import (
    BaseUserListSerializer,
    BaseUserDetailSerializer,
)


class BaseUserListViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = BaseUser.objects.all()
    serializer_class = BaseUserListSerializer


class BaseUserDetailViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    lookup_field = "id"
    queryset = BaseUser.objects.all()
    serializer_class = BaseUserDetailSerializer
