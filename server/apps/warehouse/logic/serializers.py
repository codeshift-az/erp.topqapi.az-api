from rest_framework import serializers

from server.apps.product.logic.fields import ProductField
from server.apps.supplier.logic.fields import SupplierField
from server.apps.warehouse.models import CartItem, Entry, Product


class WarehouseProductSerializer(serializers.ModelSerializer):
    """Serializer definition for Warehouse Product model."""

    entry = serializers.PrimaryKeyRelatedField(queryset=Entry.objects.all(), write_only=True)
    product = ProductField()

    class Meta:
        model = Product
        fields = (
            "id",
            "entry",
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

    products = WarehouseProductSerializer(many=True, read_only=True)
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


class CartItemSerializer(serializers.ModelSerializer):
    """Serializer definition for CartItem model."""

    product = ProductField()

    class Meta:
        model = CartItem
        fields = (
            "id",
            "product",
            "quantity",
            "price",
            "updated_at",
            "created_at",
        )
        read_only_fields = (
            "id",
            "updated_at",
            "created_at",
        )

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
