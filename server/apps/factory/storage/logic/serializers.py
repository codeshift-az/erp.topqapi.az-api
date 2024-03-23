from rest_framework import serializers

from server.apps.factory.product.logic.fields import FactoryProductField
from server.apps.factory.storage.models import FactoryStorageItem


class FactoryStorageItemSerializer(serializers.ModelSerializer):
    """Serializer definition for FactoryStorageItem model."""

    product = FactoryProductField()

    sale_count = serializers.IntegerField()

    class Meta:
        model = FactoryStorageItem
        fields = (
            "id",
            "product",
            "quantity",
            "sale_count",
            "price",
            "date",
            "updated_at",
            "created_at",
        )
        read_only_fields = (
            "id",
            "updated_at",
            "created_at",
        )
