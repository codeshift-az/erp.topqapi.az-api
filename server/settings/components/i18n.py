"""
Internationalization settings.

For more information, see
https://docs.djangoproject.com/en/5.1/topics/i18n/
"""

from server.settings.components import BASE_DIR
from server.settings.components.default import MIDDLEWARE

LANGUAGE_CODE = "en"

LANGUAGES = (("en", "English"),)

TIME_ZONE = "Asia/Baku"

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [
    BASE_DIR / "locale",
]

MIDDLEWARE.insert(2, "django.middleware.locale.LocaleMiddleware")
