from django_filters import rest_framework as filters

from server.apps.expense.models import Expense


class ExpenseFilter(filters.FilterSet):
    """FilterSet class for Expense model."""

    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    date_start = filters.DateFilter(field_name="date", lookup_expr="gte")
    date_end = filters.DateFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = Expense
        fields = (
            "name",
            "date_start",
            "date_end",
        )
