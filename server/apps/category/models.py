from django.db import models

from server.apps.core.models import CoreModel


class Category(CoreModel):
    """Model definition for Category."""

    name = models.CharField(max_length=255, unique=True)

    class Meta(CoreModel.Meta):
        """Meta definition for Category."""

        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        """Unicode representation of Category."""

        return self.name
