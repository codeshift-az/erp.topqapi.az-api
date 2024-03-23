from rest_framework import serializers

# Fields
from server.apps.product.logic.fields import ProductField
from server.apps.supplier.logic.fields import SupplierField

# Warehouse
from server.apps.warehouse.models import WarehouseCartItem, WarehouseEntry, WarehouseItem


class WarehouseItemSerializer(serializers.ModelSerializer):
    """Serializer definition for WarehouseItem model."""

    entry = serializers.PrimaryKeyRelatedField(queryset=WarehouseEntry.objects.all(), write_only=True)

    product = ProductField()

    supplier = SupplierField(read_only=True, source="entry.supplier")

    sale_count = serializers.IntegerField(read_only=True)

    catalog_price = serializers.SerializerMethodField(read_only=True)
    is_sold = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = WarehouseItem
        fields = (
            "id",
            "entry",
            "product",
            "supplier",
            "price",
            "quantity",
            "sale_count",
            "catalog_price",
            "is_sold",
            "updated_at",
            "created_at",
        )
        read_only_fields = (
            "id",
            "sale_count",
            "updated_at",
            "created_at",
        )

    def get_catalog_price(self, instance):
        """Get catalog price of product."""
        record = instance.product.catalog.filter(supplier=instance.entry.supplier).first()

        if record:
            return record.price

        return 0

    def get_is_sold(self, instance):
        """Check if item is sold."""
        return instance.sales.exists()


class WarehouseEntrySerializer(serializers.ModelSerializer):
    """Serializer definition for WarehouseEntry model."""

    items = WarehouseItemSerializer(many=True, read_only=True)
    supplier = SupplierField()

    class Meta:
        model = WarehouseEntry
        fields = (
            "id",
            "items",
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

    def create(self, validated_data):
        """Add Cart Items as items for WarehouseEntry"""
        entry = WarehouseEntry.objects.create(**validated_data)

        items = WarehouseCartItem.objects.filter(user=self.context["request"].user)

        for item in items:
            product = WarehouseItem.objects.create(
                entry=entry,
                product=item.product,
                price=item.price,
                quantity=item.quantity,
            )
            item.delete()
            product.save()

        return entry


class WarehouseCartItemSerializer(serializers.ModelSerializer):
    """Serializer definition for WarehouseCartItem model."""

    product = ProductField()

    class Meta:
        model = WarehouseCartItem
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


class WarehouseProductSerializer(serializers.Serializer):
    """Serializer definition for WarehouseItem Stats."""

    name = serializers.CharField()
    quantity = serializers.IntegerField()
    sale_count = serializers.IntegerField()
    last_entry = serializers.DateField()
