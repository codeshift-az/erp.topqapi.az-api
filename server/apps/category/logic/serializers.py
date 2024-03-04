from rest_framework import serializers

from server.apps.category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Serializer definition for Category model."""

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "updated_at",
            "created_at",
        )
        read_only_fields = (
            "id",
            "updated_at",
            "created_at",
        )
