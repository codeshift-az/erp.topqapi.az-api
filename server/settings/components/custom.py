# Custom Project Settings

from server.settings.components import BASE_DIR
from server.settings.components.common import INSTALLED_APPS

INSTALLED_APPS += [
    "server.apps.core",
    "server.apps.auth",
    "server.apps.user",
    "server.apps.account",
    "server.apps.category",
    "server.apps.supplier",
]

# Media files
# https://docs.djangoproject.com/en/4.2/topics/files/

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"

# Custom user model

AUTH_USER_MODEL = "user.User"
