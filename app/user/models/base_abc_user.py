from django.apps import apps
from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class BaseCustomAbstractUserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, password, **extra_fields)


class BaseCustomAbstractUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _("username"),
        max_length=25,
        unique=True,
        validators=[UnicodeUsernameValidator()],
        error_messages={
            "unique": _("Username already exists."),
        },
    )

    first_name = models.CharField(
        _("first name"),
        max_length=50,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        _("last name"),
        max_length=50,
        null=True,
        blank=True,
    )

    date_joined = models.DateTimeField(
        _("date joined"),
        default=timezone.now
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = BaseCustomAbstractUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        abstract = True

    @classmethod
    def get_email_field_name(cls):
        pass

    @property
    def get_firstname(self):
        return self.first_name.strip()

    @property
    def get_lastname(self):
        return self.last_name.strip()

    @property
    def get_fullname(self):
        return f"{self.get_lastname} {self.get_firstname}"
