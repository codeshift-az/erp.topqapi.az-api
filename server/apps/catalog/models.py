from django.db import models

from server.apps.core.models import TimeStampedModel


class CatalogItem(TimeStampedModel):
    """Model definition for CatalogItem."""

    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, related_name="catalog")
    supplier = models.ForeignKey("supplier.Supplier", on_delete=models.CASCADE, related_name="catalog")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = "Catalog Item"
        verbose_name_plural = "Catalog Items"

        ordering = ("-updated_at",)

    def __str__(self):
        """Unicode representation of CatalogItem."""
        return f"Catalog Item: {self.product.name} ({self.supplier.name}) - {self.price}"
