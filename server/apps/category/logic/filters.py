from django_filters import rest_framework as filters

from server.apps.category.models import Category


class CategoryFilter(filters.FilterSet):
    """FilterSet class for Category model."""

    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Category
        fields = ("name",)
