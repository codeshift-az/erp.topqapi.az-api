from django.contrib import admin

from server.apps.factory.storage.models import FactoryStorageItem


@admin.register(FactoryStorageItem)
class FactoryStorageItemAdmin(admin.ModelAdmin):
    """Admin class for FactoryStorageItem model."""

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
