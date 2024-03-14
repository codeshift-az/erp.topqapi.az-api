from django_filters import rest_framework as filters

from server.apps.order.models import Order, OrderItem


class OrderItemFilter(filters.FilterSet):
    """FilterSet class for OrderItem model."""

    product = filters.CharFilter(field_name="product__name", lookup_expr="icontains")
    supplier = filters.CharFilter(field_name="supplier__name", lookup_expr="icontains")

    class Meta:
        model = OrderItem
        fields = (
            "product",
            "supplier",
        )


class OrderFilter(filters.FilterSet):
    """FilterSet class for Order model."""

    date_start = filters.DateFilter(field_name="date", lookup_expr="gte")
    date_end = filters.DateFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = Order
        fields = (
            "customer",
            "phone",
            "status",
            "date_start",
            "date_end",
        )
