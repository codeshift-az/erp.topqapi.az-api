from rest_framework import serializers

from server.apps.branch.logic.fields import BranchField
from server.apps.order.models import Order, OrderCartItem, OrderItem
from server.apps.product.logic.fields import ProductField
from server.apps.staff.logic.fields import DriverField, SellerField, WorkerField
from server.apps.supplier.logic.fields import SupplierField


class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer definition for  OrderItem model."""

    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all(), write_only=True)
    product = ProductField()
    supplier = SupplierField()

    class Meta:
        model = OrderItem
        fields = (
            "id",
            "order",
            "product",
            "supplier",
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


class OrderSerializer(serializers.ModelSerializer):
    """Serializer definition for Order model."""

    items = OrderItemSerializer(many=True, read_only=True)

    branch = BranchField()
    seller = SellerField()

    driver = DriverField()

    worker = WorkerField()

    class Meta:
        model = Order
        fields = (
            "id",
            "items",
            "branch",
            "seller",
            "customer",
            "phone",
            "address",
            "note",
            "discount",
            "payed",
            "seller_share",
            "sale_date",
            "driver",
            "delivery_date",
            "worker",
            "install_date",
            "status",
            "updated_at",
            "created_at",
        )
        read_only_fields = (
            "id",
            "updated_at",
            "created_at",
        )

    def create(self, validated_data):
        """Add Cart Items as products for Order"""
        order = Order.objects.create(**validated_data)

        items = OrderCartItem.objects.filter(user=self.context["request"].user)

        for item in items:
            product = OrderItem.objects.create(
                order=order,
                product=item.product,
                supplier=item.supplier,
                price=item.price,
                quantity=item.quantity,
            )
            item.delete()
            product.save()

        return order


class OrderCartItemSerializer(serializers.ModelSerializer):
    """Serializer definition for OrderCartItem model."""

    product = ProductField()
    supplier = SupplierField()

    class Meta:
        model = OrderCartItem
        fields = (
            "id",
            "product",
            "supplier",
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
