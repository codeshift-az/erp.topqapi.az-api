from django.db import models

from server.apps.core.models import TimeStampedModel


class Payment(TimeStampedModel):
    """Model definition for Payment."""

    supplier = models.ForeignKey("supplier.Supplier", on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateField()

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

        ordering = ("-updated_at",)

    def __str__(self):
        """Unicode representation of Payment."""
        return f"{self.supplier.name}: {self.amount}"
