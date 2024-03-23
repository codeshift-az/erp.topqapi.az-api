from django_filters import rest_framework as filters

from server.apps.factory.sale.models import FactorySale


class FactorySaleFilter(filters.FilterSet):
    """FilterSet class for FactorySale model."""

    product = filters.CharFilter(field_name="product__name", lookup_expr="icontains")
    date_start = filters.DateFilter(field_name="date", lookup_expr="gte")
    date_end = filters.DateFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = FactorySale
        fields = (
            "product",
            "date_start",
            "date_end",
        )
