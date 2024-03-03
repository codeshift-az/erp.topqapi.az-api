from django.contrib import admin

from server.apps.product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin class for Product model."""

    list_display = (
        "name",
        "category",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "category",
        "updated_at",
        "created_at",
    )
    search_fields = ("name",)
