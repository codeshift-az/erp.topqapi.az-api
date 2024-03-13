from django.contrib import admin

from server.apps.order.models import Order, OrderItem


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


class OrderItemInline(admin.TabularInline):
    """Admin Inline class for OrderItem Model."""

    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Admin class for Order model."""

    inlines = (OrderItemInline,)

    list_display = (
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
    list_filter = (
        "date",
        "updated_at",
        "created_at",
    )
    search_fields = ("supplier_name",)
