from django_filters import rest_framework as filters

from server.apps.product.models import Product


class ProductFilter(filters.FilterSet):
    """FilterSet class for Product model."""

    id = filters.NumberFilter(field_name="id", lookup_expr="exact")
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    category = filters.CharFilter(field_name="category__name", lookup_expr="icontains")

    class Meta:
        model = Product
        fields = ("id", "name", "category")
