from django.contrib import admin

from server.apps.catalog.models import ProductRecord


@admin.register(ProductRecord)
class ProductRecordAdmin(admin.ModelAdmin):
    """Admin class for ProductRecord model."""

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
