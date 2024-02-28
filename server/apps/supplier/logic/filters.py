from django_filters import rest_framework as filters

from server.apps.supplier.models import Supplier


class SupplierFilter(filters.FilterSet):
    """FilterSet class for Supplier model."""

    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Supplier
        fields = ("name",)
