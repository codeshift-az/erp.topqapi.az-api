from rest_framework import serializers

from server.apps.catalog.models import CatalogItem
from server.apps.product.logic.fields import ProductField
from server.apps.supplier.logic.fields import SupplierField


class CatalogItemSerializer(serializers.ModelSerializer):
    """Serializer definition for CatalogItem model."""

    product = ProductField()
    supplier = SupplierField()

    class Meta:
        model = CatalogItem
        fields = (
            "id",
            "product",
            "supplier",
            "price",
            "updated_at",
            "created_at",
        )
        read_only_fields = (
            "id",
            "updated_at",
            "created_at",
        )
