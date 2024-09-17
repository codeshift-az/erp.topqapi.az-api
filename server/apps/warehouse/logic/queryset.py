from django.db import models

from server.apps.order.models import OrderItemSale


class WarehouseItemQuerySet(models.QuerySet):
    """QuerySet definition for WarehouseItem model."""

    def get_related(self):
        """Select/Prefetch all relations."""
        return self.select_related(
            "product",
            "product__category",
        ).prefetch_related(
            "product__catalog",
            "sales",
        )

    def get_sales(self):
        """Get Sales of every item."""
        return self.annotate(
            sale_count=models.Sum("sales__quantity", default=0), left=models.F("quantity") - models.F("sale_count")
        )

    def get_stats(self):
        """Get stats of all items."""

        return self.get_sales().aggregate(
            total_quantity=models.Sum("quantity"),
            total_sale_count=models.Sum("sale_count"),
            total_investment=models.Sum(models.F("quantity") * models.F("price")),
            total_investment_left=models.Sum((models.F("quantity") - models.F("sale_count")) * models.F("price")),
        )

    def get_product_stats(self):
        """Get Stats of every unique product."""
        sale_count_sub = models.Subquery(
            OrderItemSale.objects.filter(order_item__product=models.OuterRef("product"))
            .values("order_item__product")
            .annotate(sale_count=models.Sum("quantity"))
            .values("sale_count")
        )

        return (
            self.values("product")
            .annotate(
                name=models.F("product__name"),
                category=models.F("product__category__name"),
                quantity=models.Sum("quantity"),
                sale_count=sale_count_sub,
                last_entry=models.Max("entry__date"),
            )
            .order_by("-last_entry")
        )
