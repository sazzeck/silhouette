import os
import sys

from pathlib import Path

from utils import Config as config


BASE_DIR = Path(__file__).resolve().parent.parent.parent

RUN_SERVER_PORT = 8080

INSTALLED_APPS = [
    "main",
    "user",
    "rest_framework",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "silhouette.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "silhouette.wsgi.application"


REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DATETIME_FORMAT": "%d.%m.%Y %H:%M",
}


DATE_INPUT_FORMATS = ["%d.%m.%Y %H:%M"]
DATE_FORMAT = ["%d.%m.%Y %H:%M"]

TIME_ZONE = "Europe/Kiev"

USE_I18N = True

USE_TZ = True


CSRF_USE_SESSIONS = True


LANGUAGE_CODE = "en-us"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


AUTH_USER_MODEL = "user.BaseUser"

LOGIN_URL = "account/sing_in/"


SECRET_KEY = config.SECRET_KEY


STATIC_URL = "/static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

if sys.argv[1] != 'runserver':
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "main/static"),
        os.path.join(BASE_DIR, "user/static"),
    ]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
