from django.db import models

from server.apps.core.models import CoreModel


class Supplier(CoreModel):
    """Model definition for Supplier."""

    name = models.CharField(max_length=255, unique=True)

    class Meta(CoreModel.Meta):
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"

    def __str__(self):
        """Unicode representation of Supplier."""

        return self.name
