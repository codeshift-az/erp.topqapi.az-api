from django_filters import rest_framework as filters

from server.apps.branch.models import Branch


class BranchFilter(filters.FilterSet):
    """FilterSet class for Branch model."""

    id = filters.NumberFilter(field_name="id", lookup_expr="exact")
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Branch
        fields = (
            "id",
            "name",
        )
