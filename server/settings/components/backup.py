"""
Backup settings.
"""

from server.settings.components import config
from server.settings.components.default import INSTALLED_APPS

# django-dbbackup
# https://django-dbbackup.readthedocs.io/en/stable/index.html

INSTALLED_APPS += ["dbbackup"]

DBBACKUP_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
DBBACKUP_STORAGE_OPTIONS = {
    "access_key": config("AWS_ACCESS_KEY", cast=str, default=""),
    "secret_key": config("AWS_SECRET_KEY", cast=str, default=""),
    "bucket_name": config("AWS_BUCKET_NAME", cast=str, default=""),
    "location": f'{config("AWS_FOLDER_NAME", cast=str, default="")}/',
    "default_acl": "private",
}

DBBACKUP_CLEANUP_KEEP = 10
DBBACKUP_CLEANUP_KEEP_MEDIA = 10

# django-crontab
# https://github.com/kraiz/django-crontab

INSTALLED_APPS += ["django_crontab"]

CRONJOBS = [
    # Backup the database every 6 hours.
    ("0 */6 * * *", "django.core.management.call_command", ["backup"]),
]
