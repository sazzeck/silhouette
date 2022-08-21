from django.db import models
from django.utils.translation import gettext_lazy as _

from .base_abc_user import BaseCustomAbstractUser


class BaseUser(BaseCustomAbstractUser):

    is_online = models.BooleanField(
        _("is online"),
        default=False,
    )

    class Meta:
        db_table = "users"
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = [
            "id",
            "username",
            "date_joined",
            "is_online"
        ]

    def __str__(self):
        return self.username
