from django_filters import rest_framework as filters

from server.apps.payment.models import Payment


class PaymentFilter(filters.FilterSet):
    """FilterSet class for Payment model."""

    id = filters.NumberFilter(field_name="id", lookup_expr="exact")
    supplier = filters.CharFilter(field_name="supplier__name", lookup_expr="icontains")
    date_start = filters.DateFilter(field_name="date", lookup_expr="gte")
    date_end = filters.DateFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = Payment
        fields = (
            "id",
            "supplier",
            "date_start",
            "date_end",
        )
