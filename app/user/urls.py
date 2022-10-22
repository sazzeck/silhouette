from django.urls import path, include
from rest_framework import routers

from .views import (
    BaseUserDetailViewSet,
    BaseUserListViewSet,
    SingInUserView,
    SingOutUserView,
)


router = routers.DefaultRouter()
router.register(r"user", BaseUserDetailViewSet)
router.register(r"user", BaseUserListViewSet)

urlpatterns = [
    path("account/sing_in/", SingInUserView.as_view(), name="sing_in"),
    path("accounts/sing_out/", SingOutUserView.as_view(), name="sing_out"),
    path("api/v1/", include(router.urls)),
]
