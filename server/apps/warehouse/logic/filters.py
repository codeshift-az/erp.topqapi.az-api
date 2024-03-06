from django_filters import rest_framework as filters

from server.apps.warehouse.models import Entry, Product


class ProductFilter(filters.FilterSet):
    """FilterSet class for Product model."""

    product = filters.CharFilter(field_name="product__name", lookup_expr="icontains")

    class Meta:
        model = Product
        fields = ("product",)


class EntryFilter(filters.FilterSet):
    """FilterSet class for Entry model."""

    supplier = filters.CharFilter(field_name="supplier__name", lookup_expr="icontains")
    date_start = filters.DateFilter(field_name="date", lookup_expr="gte")
    date_end = filters.DateFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = Entry
        fields = (
            "supplier",
            "date_start",
            "date_end",
        )
