from django.contrib.auth.models import AbstractUser
from django.db import models


class UserTypes(models.IntegerChoices):
    """User types."""

    USER = 0, "İstifadəçi"
    ADMIN = 1, "Müdür"
    WAREHOUSE = 2, "Anbar"
    STORE = 3, "Mağaza"


class User(AbstractUser):
    """Custom user model."""

    type = models.PositiveSmallIntegerField(choices=UserTypes.choices, default=UserTypes.USER)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def save(self, *args, **kwargs):
        """Save user permissions and type."""
        if self.type in [UserTypes.WAREHOUSE, UserTypes.STORE]:
            self.is_staff = True
            self.is_superuser = False

        if self.type == UserTypes.ADMIN:
            self.is_staff = True
            self.is_superuser = True

        if not self.type and self.is_superuser:
            self.type = UserTypes.ADMIN

        super().save(*args, **kwargs)
