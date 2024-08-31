"""
Project Related settings.
"""

from server.settings.components.default import INSTALLED_APPS

INSTALLED_APPS += [
    "server.apps.core",
    "server.apps.auth",
    "server.apps.user",
    "server.apps.account",
    "server.apps.category",
    "server.apps.supplier",
    "server.apps.branch",
    "server.apps.staff",
    "server.apps.product",
    "server.apps.expense",
    "server.apps.catalog",
    "server.apps.warehouse",
    "server.apps.order",
    "server.apps.payment",
]

# Custom user model

AUTH_USER_MODEL = "user.User"
