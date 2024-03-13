from rest_framework import serializers

from server.apps.catalog.models import ProductRecord
from server.apps.product.logic.fields import ProductField
from server.apps.supplier.logic.fields import SupplierField


class ProductRecordSerializer(serializers.ModelSerializer):
    """Serializer definition for ProductRecord model."""

    product = ProductField()
    supplier = SupplierField()

    class Meta:
        model = ProductRecord
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
