"""
Production environment settings.
"""

from server.settings.components import config

SECRET_KEY = config("DJANGO_SECRET_KEY", cast=str)

DEBUG = False

ALLOWED_HOSTS = [
    f'*.{config("DOMAIN_NAME", cast=str)}',
    config("DOMAIN_NAME", cast=str),
    # We need this value for `healthcheck` to work:
    "localhost",
]

# Staticfiles
# https://docs.djangoproject.com/en/5.1/ref/contrib/staticfiles/

STATIC_ROOT = "/var/www/static"

# Media files
# https://docs.djangoproject.com/en/5.1/topics/files/

MEDIA_ROOT = "/var/www/media"

# Security
# https://docs.djangoproject.com/en/5.1/topics/security/

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SECURE_REDIRECT_EXEMPT = [
    # This is required for healthcheck to work:
    "^health/",
]

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
