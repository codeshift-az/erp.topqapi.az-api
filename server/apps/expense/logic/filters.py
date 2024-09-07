from django_filters import rest_framework as filters

from server.apps.expense.models import Expense


class ExpenseFilter(filters.FilterSet):
    """FilterSet class for Expense model."""

    id = filters.NumberFilter(field_name="id", lookup_expr="exact")
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    branch = filters.CharFilter(field_name="branch__name", lookup_expr="icontains")
    branch_id = filters.NumberFilter(field_name="branch__id", lookup_expr="exact")

    date = filters.DateFilter(field_name="date", lookup_expr="exact")
    date_start = filters.DateFilter(field_name="date", lookup_expr="gte")
    date_end = filters.DateFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = Expense
        fields = (
            "id",
            "name",
            "branch",
            "date_start",
            "date_end",
        )
