from django_filters import rest_framework as filters

from server.apps.branch.models import Branch


class BranchFilter(filters.FilterSet):
    """FilterSet class for Branch model."""

    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Branch
        fields = ("name",)
