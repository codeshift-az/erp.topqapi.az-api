from django_filters import rest_framework as filters

from server.apps.catalog.models import ProductRecord


class ProductRecordFilter(filters.FilterSet):
    """FilterSet class for ProductRecord model."""

    product = filters.CharFilter(field_name="product__name", lookup_expr="icontains")
    supplier = filters.CharFilter(field_name="supplier__name", lookup_expr="icontains")

    class Meta:
        model = ProductRecord
        fields = ("product", "supplier")
