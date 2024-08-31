from django.contrib import admin

from server.apps.catalog.models import CatalogItem


@admin.register(CatalogItem)
class CatalogItemAdmin(admin.ModelAdmin):
    """Admin class for CatalogItem model."""

    list_display = (
        "product",
        "supplier",
        "price",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "product__category",
        "supplier",
        "updated_at",
        "created_at",
    )
    search_fields = ("product__name",)
