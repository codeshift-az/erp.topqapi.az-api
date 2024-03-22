from django.db import models


class WarehouseItemQuerySet(models.QuerySet):
    """QuerySet definition for WarehouseItem model."""

    def get_related(self):
        """Select/Prefetch all relations."""
        return self.select_related(
            "product",
            "product__category",
        ).prefetch_related(
            "sales",
        )

    def get_sales(self):
        """Get Sales of every item."""
        return self.annotate(
            sale_count=models.Sum("sales__quantity", default=0), left=models.F("quantity") - models.F("sale_count")
        )

    def get_product_stats(self):
        """Get Stats of every unique product."""
        return (
            self.values("product")
            .annotate(
                name=models.F("product__name"),
                quantity=models.Sum("quantity"),
                sale_count=models.Sum("sales__quantity", default=0),
                last_entry=models.Max("entry__date"),
            )
            .order_by("-last_entry")
        )
