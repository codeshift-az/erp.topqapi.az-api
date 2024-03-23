from django.contrib import admin

from server.apps.factory.sale.models import FactorySale, FactorySaleItem


@admin.register(FactorySale)
class FactorySaleAdmin(admin.ModelAdmin):
    """Admin class for FactorySale model."""

    list_display = (
        "product",
        "quantity",
        "price",
        "date",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "product",
        "price",
        "date",
        "updated_at",
        "created_at",
    )
    search_fields = ("product",)


@admin.register(FactorySaleItem)
class FactorySaleItemAdmin(admin.ModelAdmin):
    """Admin class for FactorySaleItem model."""

    list_display = (
        "sale",
        "storage",
        "quantity",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "updated_at",
        "created_at",
    )
