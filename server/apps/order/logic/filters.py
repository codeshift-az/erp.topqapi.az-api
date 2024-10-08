from django_filters import rest_framework as filters

from server.apps.order.models import Order, OrderItem


class OrderItemFilter(filters.FilterSet):
    """FilterSet class for OrderItem model."""

    id = filters.NumberFilter(field_name="id", lookup_expr="exact")

    product = filters.CharFilter(field_name="product__name", lookup_expr="icontains")
    supplier = filters.CharFilter(field_name="supplier__name", lookup_expr="icontains")
    category = filters.CharFilter(field_name="product__category__name", lookup_expr="icontains")

    is_sold = filters.BooleanFilter(field_name="sales", lookup_expr="isnull", exclude=True)

    date = filters.DateFilter(field_name="order__sale_date", lookup_expr="exact")
    date_start = filters.DateFilter(field_name="order__sale_date", lookup_expr="gte")
    date_end = filters.DateFilter(field_name="order__sale_date", lookup_expr="lte")

    class Meta:
        model = OrderItem
        fields = (
            "id",
            "product",
            "supplier",
            "category",
            "is_sold",
            "date_start",
            "date_end",
        )


class OrderFilter(filters.FilterSet):
    """FilterSet class for Order model."""

    id = filters.CharFilter(field_name="id", lookup_expr="icontains")

    branch = filters.CharFilter(field_name="branch__name", lookup_expr="icontains")
    branch_id = filters.NumberFilter(field_name="branch__id", lookup_expr="exact")
    seller = filters.CharFilter(field_name="seller__name", lookup_expr="icontains")

    sale_date = filters.DateFilter(field_name="sale_date", lookup_expr="exact")
    sale_date_start = filters.DateFilter(field_name="sale_date", lookup_expr="gte")
    sale_date_end = filters.DateFilter(field_name="sale_date", lookup_expr="lte")

    customer = filters.CharFilter(field_name="customer", lookup_expr="icontains")
    phone = filters.CharFilter(field_name="phone", lookup_expr="icontains")

    driver = filters.CharFilter(field_name="driver__name", lookup_expr="icontains")

    delivery_date = filters.DateFilter(field_name="delivery_date", lookup_expr="exact")
    delivery_date_start = filters.DateFilter(field_name="delivery_date", lookup_expr="gte")
    delivery_date_end = filters.DateFilter(field_name="delivery_date", lookup_expr="lte")

    worker = filters.CharFilter(field_name="worker__name", lookup_expr="icontains")

    install_date = filters.DateFilter(field_name="install_date", lookup_expr="exact")
    install_date_start = filters.DateFilter(field_name="install_date", lookup_expr="gte")
    install_date_end = filters.DateFilter(field_name="install_date", lookup_expr="lte")

    status = filters.CharFilter(field_name="status", lookup_expr="exact")

    class Meta:
        model = Order
        fields = (
            "id",
            "customer",
            "phone",
            "branch",
            "seller",
            "sale_date_start",
            "sale_date_end",
            "driver",
            "delivery_date_start",
            "delivery_date_end",
            "worker",
            "install_date_start",
            "install_date_end",
            "status",
        )
