"""
Database settings.

For more information, see
https://docs.djangoproject.com/en/5.1/ref/settings/#databases
"""

from server.settings.components import config
from server.settings.components.default import INSTALLED_APPS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_DB", cast=str, default=None),
        "USER": config("POSTGRES_USER", cast=str, default=None),
        "PASSWORD": config("POSTGRES_PASSWORD", cast=str, default=None),
        "HOST": config("POSTGRES_HOST", cast=str, default="localhost"),
        "PORT": config("POSTGRES_PORT", cast=str, default="5432"),
        "TEST": {
            "NAME": "test_db",
        },
    }
}

# django-cleanup
# https://github.com/un1t/django-cleanup

INSTALLED_APPS += ["django_cleanup.apps.CleanupConfig"]

# django-solo
# https://github.com/lazybird/django-solo

INSTALLED_APPS += ["solo"]
