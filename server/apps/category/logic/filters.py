from django_filters import rest_framework as filters

from server.apps.category.models import Category


class CategoryFilter(filters.FilterSet):
    """FilterSet class for Category model."""

    id = filters.NumberFilter(field_name="id", lookup_expr="exact")
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
        )
