from rest_framework import serializers

from server.apps.product.logic.fields import ProductField
from server.apps.supplier.logic.fields import SupplierField
from server.apps.warehouse.models import Entry, Product


class ProductSerializer(serializers.ModelSerializer):
    """Serializer definition for Product model."""

    product = ProductField()

    class Meta:
        model = Product
        fields = (
            "id",
            "product",
            "price",
            "quantity",
            "updated_at",
            "created_at",
        )
        read_only_fields = (
            "id",
            "updated_at",
            "created_at",
        )


class EntrySerializer(serializers.ModelSerializer):
    """Serializer definition for Entry model."""

    products = ProductSerializer(many=True)
    supplier = SupplierField()

    class Meta:
        model = Entry
        fields = (
            "id",
            "products",
            "supplier",
            "invoice",
            "date",
            "updated_at",
            "created_at",
        )
        read_only_fields = (
            "id",
            "updated_at",
            "created_at",
        )
