from django_filters import rest_framework as filters

from server.apps.supplier.models import Supplier


class SupplierFilter(filters.FilterSet):
    """FilterSet class for Supplier model."""

    id = filters.NumberFilter(field_name="id", lookup_expr="exact")
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    product = filters.NumberFilter(method="filter_by_product")

    class Meta:
        model = Supplier
        fields = ("name",)

    def filter_by_product(self, queryset, name, value):
        return queryset.filter(catalog__product=value)
