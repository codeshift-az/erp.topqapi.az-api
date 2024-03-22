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


class SupplierPayment(CoreModel):
    """Model definition for SupplierPayment."""

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date = models.DateField()

    class Meta(CoreModel.Meta):
        verbose_name = "SupplierPayment"
        verbose_name_plural = "SupplierPayments"

    def __str__(self):
        """Unicode representation of SupplierPayment."""
        return f"{self.supplier.name}: {self.amount} AZN"
