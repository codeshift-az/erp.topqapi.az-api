"""
Development environment settings.
"""

import socket

from server.settings.components import config
from server.settings.components.default import INSTALLED_APPS, MIDDLEWARE
from server.settings.components.logging import LOGGING

SECRET_KEY = config("DJANGO_SECRET_KEY", cast=str, default="django-insecure-abcdefghijklmnopqrstuvwxyz1234567890")

DEBUG = True

ALLOWED_HOSTS = [
    f'*.{config("DOMAIN_NAME", cast=str)}',
    config("DOMAIN_NAME", cast=str),
    "localhost",
    "127.0.0.1",
    "[::1]",
]

# Django Debug Toolbar
# https://django-debug-toolbar.readthedocs.io/en/latest/

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": [
        "debug_toolbar.panels.profiling.ProfilingPanel",
        "debug_toolbar.panels.redirects.RedirectsPanel",
    ],
    "SHOW_TEMPLATE_CONTEXT": True,
}

# Logging

LOGGING["loggers"]["server"]["level"] = "DEBUG"
LOGGING["loggers"]["server"]["handlers"] = ["console"]
LOGGING["handlers"]["console"]["level"] = "DEBUG"
