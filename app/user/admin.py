from lib2to3.pytree import Base
from django.contrib.admin import register, ModelAdmin

from .models import BaseUser


@register(BaseUser)
class BaseUserAdmin(ModelAdmin):
    list_display = (
        "id",
        "username",
        "last_login",
        "date_joined",
        "is_active",
        "is_staff",
        "is_online",
    )

    list_display_links = ("username",)

    search_fields = ("username",)

    list_filter = (
        "is_online",
        "is_active",
        "is_staff",
        "last_login",
    )

    list_editable = (
        "is_active",
        "is_staff",
    )
