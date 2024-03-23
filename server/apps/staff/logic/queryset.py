import datetime

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
        # From first of the month
        return self.annotate(
            total_orders=models.Count("orders"),
            last_month=models.Count(
                "orders",
                filter=models.Q(
                    orders__delivery_date__gte=datetime.datetime.now().replace(
                        day=1, month=datetime.datetime.now().month - 1
                    ),
                    orders__delivery_date__lt=datetime.datetime.now().replace(day=1),
                ),
            ),
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
            last_month=models.Count(
                "orders",
                filter=models.Q(
                    orders__sale_date__gte=datetime.datetime.now().replace(
                        day=1, month=datetime.datetime.now().month - 1
                    ),
                    orders__sale_date__lt=datetime.datetime.now().replace(day=1),
                ),
            ),
            total_share=models.Sum("orders__seller_share", default=0),
            last_month_share=models.Sum(
                "orders__seller_share",
                filter=models.Q(
                    orders__sale_date__gte=datetime.datetime.now().replace(
                        day=1, month=datetime.datetime.now().month - 1
                    ),
                    orders__sale_date__lt=datetime.datetime.now().replace(day=1),
                ),
                default=0,
            ),
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
            last_month=models.Count(
                "orders",
                filter=models.Q(
                    orders__install_date__gte=datetime.datetime.now().replace(
                        day=1, month=datetime.datetime.now().month - 1
                    ),
                    orders__install_date__lt=datetime.datetime.now().replace(day=1),
                ),
            ),
        )
