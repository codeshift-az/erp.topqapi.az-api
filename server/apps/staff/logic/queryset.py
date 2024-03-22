from django.db import models


class DriverQuerySet(models.QuerySet):
    """QuerySet for Driver model."""

    def get_related(self):
        """Get queryset with related fields."""
        return self.prefetch_related(
            "orders",
        )

    def get_order_stats(self):
        """Get queryset with order stats of driver."""
        return self.annotate(
            total_orders=models.Count("orders"),
        )


class SellerQuerySet(models.QuerySet):
    """QuerySet for Seller model."""

    def get_related(self):
        """Get queryset with related fields."""
        return self.select_related(
            "branch",
            "branch__user",
        ).prefetch_related(
            "orders",
        )

    def get_order_stats(self):
        """Get queryset with order stats of seller."""
        return self.annotate(
            total_orders=models.Count("orders"),
            total_share=models.Sum("orders__seller_share", default=0),
        )


class WorkerQuerySet(models.QuerySet):
    """QuerySet for Worker model."""

    def get_related(self):
        """Get queryset with related fields."""
        return self.prefetch_related(
            "orders",
        )

    def get_order_stats(self):
        """Get queryset with order stats of worker."""
        return self.annotate(
            total_orders=models.Count("orders"),
        )
