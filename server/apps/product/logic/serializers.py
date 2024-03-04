from rest_framework import serializers

from server.apps.category.logic.fields import CategoryField
from server.apps.product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Serializer definition for Product model."""

    category = CategoryField()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "category",
            "updated_at",
            "created_at",
        )
        read_only_fields = (
            "id",
            "updated_at",
            "created_at",
        )
