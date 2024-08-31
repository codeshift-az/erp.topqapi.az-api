"""
Split Settings Module.

This module is responsible for loading the all component setting files and
correct settings file based on the environment variable DJANGO_ENV.
The default value is 'local', so if you don't specify
the environment variable, the local settings will be loaded.

For more information, see the documentation:
https://django-split-settings.readthedocs.io/en/latest/
"""

from split_settings.tools import include

from server.settings.components import config

ENV = config("DJANGO_ENV", default="local", cast=str) or "local"

base_settings = (
    "components/default.py",  # Default Django Settings.
    "components/files.py",  # File related settings.
    "components/i18n.py",  # Internationalization settings.
    "components/logging.py",  # Logging settings.
    "components/database.py",  # Database settings.
    "components/backup.py",  # Backup settings.
    "components/health.py",  # Health Check settings.
    "components/corsheaders.py",  # Django CORS Headers settings.
    "components/email.py",  # Email settings.
    "components/restframework.py",  # Django REST Framework settings.
    "components/project.py",  # Project Related settings.
    f"environments/{ENV}.py",  # Environment settings.
)

include(*base_settings)
