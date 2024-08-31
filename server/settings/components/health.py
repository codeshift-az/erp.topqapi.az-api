"""
Django Health Check settings.

For more information, see
https://django-health-check.readthedocs.io/en/latest/
"""

from server.settings.components.default import INSTALLED_APPS

INSTALLED_APPS += [
    "health_check",
    "health_check.db",
    "health_check.cache",
    "health_check.contrib.migrations",
]

# Health Check URL

HEALTH_CHECK_URL = "health/"
