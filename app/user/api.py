from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from user.models import BaseUser
from user.serializers import (
    BaseUserListSerializer,
    BaseUserDetailSerializer,
)


class BaseUserViewSet(viewsets.ViewSet):

    def user_list(self, request):
        queryset = BaseUser.objects.all()
        serializer = BaseUserListSerializer(queryset, many=True)
        return Response(serializer.data)

    def user_detail(self, request, id=None):
        queryset = BaseUser.objects.all()
        user = get_object_or_404(queryset, pk=id)
        serializer = BaseUserDetailSerializer(user)
        return Response(serializer.data)
