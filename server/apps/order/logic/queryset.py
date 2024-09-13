from django.db import models

from server.apps.order.logic.constants import OrderStatus


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
            profit=models.Case(
                models.When(
                    order__status__gte=OrderStatus.READY,
                    then=models.ExpressionWrapper(
                        models.F("price") * models.F("quantity")
                        - models.Sum(models.F("sales__warehouse_item__price") * models.F("quantity")),
                        output_field=models.DecimalField(),
                    ),
                ),
                output_field=models.DecimalField(),
            ),
        )

    def get_stats(self):
        """Get Stats of the item."""
        return self.get_profit().aggregate(
            total_quantity=models.Sum(models.F("quantity"), output_field=models.DecimalField()),
            total_price=models.Sum(models.F("price") * models.F("quantity"), output_field=models.DecimalField()),
            total_profit=models.Sum(models.F("profit"), output_field=models.DecimalField(), default=0),
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
            "expenses",
        )

    def get_related_sum(self):
        """Get Sum of the related items."""

        from server.apps.order.models import OrderItem  # noqa

        total_price_sub = models.Subquery(
            OrderItem.objects.values("order")
            .annotate(total_price=models.Sum(models.F("price") * models.F("quantity")))
            .filter(order=models.OuterRef("pk"))
            .values("total_price")
        )

        total_warehouse_price_sub = models.Subquery(
            OrderItem.objects.values("order")
            .annotate(
                total_warehouse_price=models.Sum(models.F("sales__warehouse_item__price") * models.F("quantity"))
            )
            .filter(order=models.OuterRef("pk"))
            .values("total_warehouse_price")
        )

        return self.get_related().annotate(
            total_price=total_price_sub,
            total_warehouse_price=total_warehouse_price_sub,
            total_expense=models.Sum(
                models.F("expenses__price"),
                output_field=models.DecimalField(),
                distinct=True,
                default=0.00,
            ),
        )

    def get_profit(self):
        """Get Profit of the order."""
        return self.get_related_sum().annotate(
            profit=(
                models.ExpressionWrapper(
                    models.Case(
                        models.When(
                            status__gte=OrderStatus.READY,
                            then=models.ExpressionWrapper(
                                models.F("total_price")
                                - models.F("total_warehouse_price")
                                - models.F("total_expense")
                                - models.F("seller_share")
                                - models.F("delivery_price")
                                - models.F("install_price"),
                                output_field=models.DecimalField(),
                            ),
                        ),
                    ),
                    output_field=models.DecimalField(),
                )
            )
        )

    def get_sum_of_profits(self):
        """Get Sum of Profits of the orders"""
        return (
            self.get_profit()
            .aggregate(total_profit=models.Sum(models.F("profit"), output_field=models.DecimalField(), default=0))
            .get("total_profit", 0)
        )

    def get_stats(self):
        """Get Stats of the order."""
        return self.get_profit().aggregate(
            total_orders=models.Count("id"),
            total_amount=models.Sum(models.F("total_price"), output_field=models.DecimalField()),
            total_profit=models.Sum(models.F("profit"), output_field=models.DecimalField(), default=0),
            total_payed=models.Sum(models.F("payed"), output_field=models.DecimalField(), default=0),
        )
