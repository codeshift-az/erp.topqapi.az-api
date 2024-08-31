from django.db import models

from server.apps.core.models import TimeStampedModel

# Model Queryset
from server.apps.supplier.logic.queryset import SupplierQuerySet


class Supplier(TimeStampedModel):
    """Model definition for Supplier."""

    name = models.CharField(max_length=255, unique=True)

    objects = SupplierQuerySet.as_manager()

    class Meta:
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"

        ordering = ("-updated_at",)

    def __str__(self):
        """Unicode representation of Supplier."""
        return self.name

    def get_transactions(self):
        """Get all transactions of the supplier."""
        entries = (
            self.entries.all()
            .values("id")
            .annotate(
                amount=models.ExpressionWrapper(
                    models.Sum(models.F("items__price") * models.F("items__quantity")),
                    output_field=models.DecimalField(),
                ),
                type=models.Value(False, output_field=models.BooleanField()),
                date=models.F("date"),
            )
            .values("id", "amount", "type", "date")
        )
        payments = (
            self.payments.all()
            .values("id")
            .annotate(
                amount=models.F("amount"),
                type=models.Value(True, output_field=models.BooleanField()),
                date=models.F("date"),
            )
            .values("id", "amount", "type", "date")
        )
        return entries.union(payments).order_by("-date")
