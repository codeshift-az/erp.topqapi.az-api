from django.db import models

from server.apps.core.models import CoreModel

# Model QuerySet
from server.apps.factory.storage.logic.queryset import StorageItemQuerySet


class FactoryStorageItem(CoreModel):
    """Model definition for FactoryStorageItem."""

    product = models.ForeignKey("factory_product.FactoryProduct", on_delete=models.CASCADE, related_name="storage")
    quantity = models.PositiveSmallIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date = models.DateField()

    objects = StorageItemQuerySet.as_manager()

    class Meta(CoreModel.Meta):
        verbose_name = "Factory Storage Item"
        verbose_name_plural = "Factory Storage Items"

    def __str__(self):
        """Unicode representation of FactoryStorageItem."""
        return f"Factory Storage Item: {self.product.name} - {self.quantity}"
