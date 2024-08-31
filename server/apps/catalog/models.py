from django.db import models

from server.apps.core.models import TimeStampedModel


class ProductRecord(TimeStampedModel):
    """Model definition for ProductRecord."""

    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, related_name="catalog")
    supplier = models.ForeignKey("supplier.Supplier", on_delete=models.CASCADE, related_name="catalog")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = "ProductRecord"
        verbose_name_plural = "ProductRecords"

        ordering = ("-updated_at",)

    def __str__(self):
        """Unicode representation of ProductRecord."""
        return f"Product Record: {self.product.name} ({self.supplier.name}) - {self.price}"
