from django.contrib import admin

from server.apps.factory.usage.models import FactoryUsage, FactoryUsageItem


@admin.register(FactoryUsage)
class FactoryUsageAdmin(admin.ModelAdmin):
    """Admin class for FactoryUsage model."""

    list_display = (
        "product",
        "quantity",
        "date",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "product",
        "date",
        "updated_at",
        "created_at",
    )
    search_fields = ("product",)


@admin.register(FactoryUsageItem)
class FactoryUsageItemAdmin(admin.ModelAdmin):
    """Admin class for FactoryUsageItem model."""

    list_display = (
        "usage",
        "storage",
        "quantity",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "updated_at",
        "created_at",
    )
