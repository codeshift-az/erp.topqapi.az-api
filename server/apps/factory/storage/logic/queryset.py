from django.db import models


class StorageItemQuerySet(models.QuerySet):
    """QuerySet definition for StorageItem model."""

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
