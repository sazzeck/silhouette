from django.utils.translation import gettext_lazy as _

from .base_abc_user import BaseCustomAbstractUser


class BaseUser(BaseCustomAbstractUser):
    class Meta:
        db_table = "users"
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = [
            "id",
            "username",
            "date_joined",
        ]

    @classmethod
    def count(cls):
        return cls.objects.all().count()

    def __str__(self):
        return self.username
