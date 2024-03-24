from django.db import models


class OrderItemQuerySet(models.QuerySet):
    """QuerySet definition for OrderItem model."""

    def get_related(self):
        """Select/Prefetch all relations."""
        return self.select_related(
            "order",
            "product",
            "product__category",
            "supplier",
        ).prefetch_related(
            "sales",
            "sales__warehouse_item",
        )

    def get_profit(self):
        """Get Profit of the item."""
        return self.annotate(
            profit=models.ExpressionWrapper(
                models.F("price") * models.F("quantity")
                - models.Sum(models.F("sales__warehouse_item__price") * models.F("sales__warehouse_item__quantity")),
                output_field=models.DecimalField(),
            )
        )


class OrderQuerySet(models.QuerySet):
    """QuerySet definition for Order model."""

    def get_related(self):
        """Select/Prefetch all relations."""
        return self.select_related(
            "branch",
            "seller",
        ).prefetch_related(
            "items",
            "items__product",
            "items__product__category",
            "items__supplier",
            "items__sales",
        )
