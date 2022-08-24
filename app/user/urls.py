from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .views import BaseUserViewSet


urlpatterns = format_suffix_patterns(
    [
        path("user/", BaseUserViewSet.as_view({"get": "user_list"})),
        path("user/<int:id>", BaseUserViewSet.as_view({"get": "user_detail"})),
    ]
)
