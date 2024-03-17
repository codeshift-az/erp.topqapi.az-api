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

    branch = filters.CharFilter(field_name="branch__name", lookup_expr="icontains")
    seller = filters.CharFilter(field_name="seller__name", lookup_expr="icontains")

    customer = filters.CharFilter(field_name="customer", lookup_expr="icontains")
    phone = filters.CharFilter(field_name="phone", lookup_expr="icontains")

    driver = filters.CharFilter(field_name="driver__name", lookup_expr="icontains")
    worker = filters.CharFilter(field_name="worker__name", lookup_expr="icontains")

    date_start = filters.DateFilter(field_name="sale_date", lookup_expr="gte")
    date_end = filters.DateFilter(field_name="Sale_date", lookup_expr="lte")

    class Meta:
        model = Order
        fields = (
            "branch",
            "seller",
            "customer",
            "phone",
            "driver",
            "worker",
            "status",
            "date_start",
            "date_end",
        )
