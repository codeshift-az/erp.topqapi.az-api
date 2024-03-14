from rest_framework import serializers

from server.apps.branch.logic.fields import BranchField
from server.apps.order.models import Order, OrderItem
from server.apps.product.logic.fields import ProductField
from server.apps.staff.logic.fields import SellerField
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
            "discount",
            "note",
            "status",
            "date",
            "updated_at",
            "created_at",
        )
        read_only_fields = (
            "id",
            "updated_at",
            "created_at",
        )
