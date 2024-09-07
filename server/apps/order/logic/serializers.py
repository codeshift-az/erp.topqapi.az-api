from rest_framework import serializers

from server.apps.branch.logic.fields import BranchField
from server.apps.order.models import Order, OrderCartItem, OrderExpense, OrderItem
from server.apps.product.logic.fields import ProductField
from server.apps.staff.logic.fields import DriverField, SellerField, WorkerField
from server.apps.supplier.logic.fields import SupplierField
from server.apps.warehouse.models import WarehouseItem


class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer definition for OrderItem model."""

    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all(), write_only=True)
    product = ProductField()
    supplier = SupplierField()

    is_done = serializers.BooleanField(write_only=True)
    is_return = serializers.BooleanField(write_only=True)

    is_sold = serializers.SerializerMethodField()

    profit = serializers.IntegerField(read_only=True)

    date = serializers.DateField(source="order.sale_date", read_only=True)

    class Meta:
        model = OrderItem
        fields = (
            "id",
            "order",
            "product",
            "supplier",
            "price",
            "quantity",
            "size",
            "is_done",
            "is_return",
            "is_sold",
            "profit",
            "date",
            "updated_at",
            "created_at",
        )
        read_only_fields = (
            "id",
            "updated_at",
            "created_at",
        )

    def get_is_sold(self, obj):
        """Return if item is sold."""
        return obj.sales.exists()

    def validate(self, attrs):
        """Validate if there are enough items in warehouse for sale."""

        is_done = attrs.pop("is_done", False)

        if is_done and self.instance:
            items = (
                WarehouseItem.objects.get_related()
                .get_sales()
                .filter(
                    product=self.instance.product,
                    entry__supplier=self.instance.supplier,
                    left__gt=0,
                )
            )

            if not items or sum([item.left for item in items]) < self.instance.quantity:
                raise serializers.ValidationError("Anbarda bu məhsuldan yetərli qədər yoxdur!")

            count = self.instance.quantity
            n = 0

            while count > 0:
                self.instance.sales.create(
                    order_item=self.instance,
                    warehouse_item=items[n],
                    quantity=count if items[n].left >= count else items[n].left,
                )
                count -= items[n].left
                n += 1

        is_return = attrs.pop("is_return", False)

        if is_return and self.instance:
            items = self.instance.sales.all()

            for item in items:
                item.delete()

        return super().validate(attrs)


class OrderExpenseSerializer(serializers.ModelSerializer):
    """Serializer definition for OrderExpense model."""

    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all(), write_only=True)

    class Meta:
        model = OrderExpense
        fields = (
            "id",
            "order",
            "name",
            "price",
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
    expenses = OrderExpenseSerializer(many=True, read_only=True)

    branch = BranchField()
    seller = SellerField()

    driver = DriverField(required=False)

    worker = WorkerField(required=False)

    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    profit = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "items",
            "expenses",
            "branch",
            "seller",
            "customer",
            "phone",
            "address",
            "note",
            "payed",
            "seller_share",
            "sale_date",
            "driver",
            "delivery_price",
            "delivery_date",
            "worker",
            "install_price",
            "install_date",
            "status",
            "total_price",
            "profit",
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
                size=item.size,
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
            "size",
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
