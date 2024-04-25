from django.db import models


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
        return self.annotate(
            total_price=models.Sum(models.F("entries__items__price") * models.F("entries__items__quantity")),
            total_payed=models.Sum(models.F("payments__amount")),
        )
