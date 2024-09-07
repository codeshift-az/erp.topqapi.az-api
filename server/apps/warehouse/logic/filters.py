from django_filters import rest_framework as filters

from server.apps.warehouse.models import WarehouseEntry, WarehouseItem


class WarehouseItemFilter(filters.FilterSet):
    """FilterSet class for WarehouseItem model."""

    id = filters.NumberFilter(field_name="id", lookup_expr="exact")
    product = filters.CharFilter(field_name="product__name", lookup_expr="icontains")
    category = filters.CharFilter(field_name="product__category__name", lookup_expr="icontains")
    supplier = filters.CharFilter(field_name="entry__supplier__name", lookup_expr="icontains")

    date = filters.DateFilter(field_name="entry__date", lookup_expr="exact")
    date_start = filters.DateFilter(field_name="entry__date", lookup_expr="gte")
    date_end = filters.DateFilter(field_name="entry__date", lookup_expr="lte")

    class Meta:
        model = WarehouseItem
        fields = (
            "id",
            "product",
            "category",
            "supplier",
        )


class WarehouseEntryFilter(filters.FilterSet):
    """FilterSet class for WarehouseEntry model."""

    id = filters.NumberFilter(field_name="id", lookup_expr="exact")
    supplier = filters.CharFilter(field_name="supplier__name", lookup_expr="icontains")
    date_start = filters.DateFilter(field_name="date", lookup_expr="gte")
    date_end = filters.DateFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = WarehouseEntry
        fields = (
            "id",
            "supplier",
            "date_start",
            "date_end",
        )
