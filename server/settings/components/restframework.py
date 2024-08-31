"""
Django REST Framework settings.

For more information, see:
https://www.django-rest-framework.org/
"""

import datetime

from server.settings.components.default import INSTALLED_APPS

INSTALLED_APPS += [
    "rest_framework",
    "django_filters",
    "drf_spectacular",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
]

# REST Framework
# https://www.django-rest-framework.org/api-guide/settings/

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "server.apps.core.logic.permissions.IsAdminUserOrReadOnlyForStaff",
    ],
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.MultiPartParser",
        "rest_framework.parsers.FormParser",
    ],
    "DEFAULT_PAGINATION_CLASS": "server.apps.core.logic.pagination.PageLimitPagination",
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# Simple JWT settings
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=90),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}

# DRF Spectacular settings
# https://drf-spectacular.readthedocs.io/en/latest/

SPECTACULAR_SETTINGS = {
    "TITLE": "TopQapı API",
    "DESCRIPTION": "API for TopQapı project",
    "VERSION": "1.0.0",
    "COMPONENT_SPLIT_REQUEST": True,
    "SERVE_INCLUDE_SCHEMA": True,
}
