from rest_framework import serializers

import server.apps.category.logic.schema  # noqa: F401
from server.apps.category.logic.serializers import CategorySerializer
from server.apps.category.models import Category


class CategoryField(serializers.RelatedField):
    """Serializer definition for Category field."""

    def get_queryset(self):
        """Return queryset of Category objects."""
        return Category.objects.all()

    def to_representation(self, value: Category) -> dict:
        """Return representation of Category object."""
        return CategorySerializer(value).data

    def to_internal_value(self, data: int) -> Category:
        """Return Category object from given data."""
        category = Category.objects.get(pk=data)

        if category is None:
            return serializers.ValidationError(f"Category with id {data} does not exist.")

        return category
