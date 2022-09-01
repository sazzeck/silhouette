from rest_framework import routers

from .views import BaseUserListViewSet, BaseUserDetailViewSet


router = routers.DefaultRouter()
router.register(r"user", BaseUserDetailViewSet)
router.register(r"user", BaseUserListViewSet)

urlpatterns = router.urls
