from django.db import models

from server.apps.core.models import TimeStampedModel


class Category(TimeStampedModel):
    """Model definition for Category."""

    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

        ordering = ("-updated_at",)

    def __str__(self):
        """Unicode representation of Category."""
        return self.name
