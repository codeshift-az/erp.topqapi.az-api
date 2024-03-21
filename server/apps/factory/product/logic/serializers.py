from rest_framework import serializers

from server.apps.category.logic.fields import CategoryField
from server.apps.factory.product.models import FactoryProduct


class FactoryProductSerializer(serializers.ModelSerializer):
    """Serializer definition for FactoryProduct model."""

    category = CategoryField()

    class Meta:
        model = FactoryProduct
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
