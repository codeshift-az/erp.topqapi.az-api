from django.db import models
from django.db.models.functions import Coalesce

from server.apps.payment.models import Payment
from server.apps.warehouse.models import WarehouseEntry


class SupplierQuerySet(models.QuerySet):
    """QuerySet definition for Supplier model."""

    def get_related(self):
        """Select/Prefetch all relations."""
        return self.prefetch_related(
            "entries",
            "entries__items",
            "payments",
            "catalog",
        )

    def get_debt(self):
        """Get payments and debts of the supplier."""

        total_price = (
            WarehouseEntry.objects.filter(supplier=models.OuterRef("pk"))
            .values("supplier")
            .annotate(amount_sum=models.Sum(models.F("items__price") * models.F("items__quantity")))
            .values("amount_sum")[:1]
        )

        total_payed = (
            Payment.objects.filter(supplier=models.OuterRef("pk"))
            .values("supplier")
            .annotate(amount_sum=models.Sum(models.F("amount")))
            .values("amount_sum")[:1]
        )

        return self.annotate(
            total_price=Coalesce(models.Subquery(total_price), 0, output_field=models.DecimalField()),
            total_payed=Coalesce(models.Subquery(total_payed), 0, output_field=models.DecimalField()),
        )
