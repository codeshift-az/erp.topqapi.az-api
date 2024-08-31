"""
Django CORS Headers settings.

For more information, see
https://github.com/adamchainz/django-cors-headers
"""

import re

from server.settings.components import config
from server.settings.components.default import INSTALLED_APPS, MIDDLEWARE

INSTALLED_APPS += ["corsheaders"]

MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^http://localhost:\d+$",
]

if config("DOMAIN_NAME", default=None):
    CORS_ALLOWED_ORIGIN_REGEXES += [
        r"^https?://(([a-zA-Z0-9-])+(\.))?" + re.escape(config("DOMAIN_NAME", cast=str)) + r"$",
    ]
