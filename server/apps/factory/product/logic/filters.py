from django_filters import rest_framework as filters

from server.apps.factory.product.models import FactoryProduct


class FactoryProductFilter(filters.FilterSet):
    """FilterSet class for FactoryProduct model."""

    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    category = filters.CharFilter(field_name="category__name", lookup_expr="icontains")

    class Meta:
        model = FactoryProduct
        fields = (
            "name",
            "category",
        )
