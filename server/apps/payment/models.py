from django.db import models

from server.apps.core.models import CoreModel


class Payment(CoreModel):
    """Model definition for Payment."""

    supplier = models.ForeignKey("supplier.Supplier", on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateField()

    class Meta(CoreModel.Meta):
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    def __str__(self):
        """Unicode representation of Payment."""
        return f"{self.supplier.name}: {self.amount}"
