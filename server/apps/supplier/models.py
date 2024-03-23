from django.db import models

from server.apps.core.models import CoreModel

# Model Queryset
from server.apps.supplier.logic.queryset import SupplierQuerySet


class Supplier(CoreModel):
    """Model definition for Supplier."""

    name = models.CharField(max_length=255, unique=True)

    objects = SupplierQuerySet.as_manager()

    class Meta(CoreModel.Meta):
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"

    def __str__(self):
        """Unicode representation of Supplier."""
        return self.name
