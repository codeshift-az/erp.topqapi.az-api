from django.contrib import admin

from server.apps.order.models import Order, OrderCartItem, OrderExpense, OrderItem, OrderItemSale


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """Admin class for OrderItem model."""

    list_display = (
        "order",
        "product",
        "supplier",
        "price",
        "quantity",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "order",
        "supplier",
        "product__category",
        "updated_at",
        "created_at",
    )
    search_fields = (
        "product__name",
        "supplier__name",
    )


@admin.register(OrderExpense)
class OrderExpenseAdmin(admin.ModelAdmin):
    """Admin class for OrderExpense model."""

    list_display = (
        "order",
        "name",
        "price",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "order",
        "updated_at",
        "created_at",
    )
    search_fields = ("name",)


class OrderItemInline(admin.TabularInline):
    """Admin Inline class for OrderItem Model."""

    model = OrderItem
    extra = 1


class OrderExpenseInline(admin.TabularInline):
    """Admin Inline class for OrderItem Model."""

    model = OrderExpense
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Admin class for Order model."""

    inlines = (OrderItemInline, OrderExpenseInline)

    list_display = (
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
        "delivery_date",
        "driver",
        "install_date",
        "worker",
        "status",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "seller",
        "branch",
        "sale_date",
        "updated_at",
        "created_at",
    )
    search_fields = ("supplier_name",)


@admin.register(OrderCartItem)
class OrderCartItemAdmin(admin.ModelAdmin):
    """Admin class for OrderCartItem model."""

    list_display = (
        "product",
        "supplier",
        "price",
        "quantity",
        "user",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "user",
        "product",
        "supplier",
        "updated_at",
        "created_at",
    )
    search_fields = (
        "user__username",
        "user__first_name",
        "product__name",
        "supplier__name",
    )


@admin.register(OrderItemSale)
class OrderItemSaleAdmin(admin.ModelAdmin):
    """Admin class for OrderItemSale model."""

    list_display = (
        "order_item",
        "warehouse_item",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "updated_at",
        "created_at",
    )
