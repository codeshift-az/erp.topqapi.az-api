from django.contrib import admin

from server.apps.warehouse.models import WarehouseCartItem, WarehouseEntry, WarehouseItem


@admin.register(WarehouseItem)
class WarehouseItemAdmin(admin.ModelAdmin):
    """Admin class for WarehouseItem model."""

    list_display = (
        "product",
        "price",
        "quantity",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "product__category",
        "updated_at",
        "created_at",
    )
    search_fields = ("product__name",)


class WarehouseItemInline(admin.TabularInline):
    """Admin Inline class for WarehouseItem Model."""

    model = WarehouseItem
    extra = 1


@admin.register(WarehouseEntry)
class WarehouseEntryAdmin(admin.ModelAdmin):
    """Admin class for WarehouseEntry model."""

    inlines = (WarehouseItemInline,)

    list_display = (
        "supplier",
        "invoice",
        "date",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "supplier",
        "date",
        "updated_at",
        "created_at",
    )
    search_fields = ("supplier_name",)


@admin.register(WarehouseCartItem)
class WarehouseCartItemAdmin(admin.ModelAdmin):
    """Admin class for WarehouseCartItem model."""

    list_display = (
        "product",
        "price",
        "quantity",
        "user",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "user",
        "product",
        "updated_at",
        "created_at",
    )
    search_fields = (
        "user__username",
        "user__first_name",
        "product__name",
    )
