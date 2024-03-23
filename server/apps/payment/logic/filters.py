from django_filters import rest_framework as filters

from server.apps.payment.models import Payment


class PaymentFilter(filters.FilterSet):
    """FilterSet class for Payment model."""

    supplier = filters.CharFilter(field_name="supplier__name", lookup_expr="icontains")
    date_start = filters.DateFilter(field_name="date", lookup_expr="gte")
    date_end = filters.DateFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = Payment
        fields = (
            "supplier",
            "date_start",
            "date_end",
        )
