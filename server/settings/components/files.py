"""
File related settings.
"""

from server.settings.components import BASE_DIR

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

# Media files
# https://docs.djangoproject.com/en/5.1/topics/files/

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"
