from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom user model."""

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
