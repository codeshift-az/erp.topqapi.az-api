from django.contrib import admin

from server.apps.factory.product.models import FactoryProduct


@admin.register(FactoryProduct)
class FactoryProductAdmin(admin.ModelAdmin):
    """Admin class for FactoryProduct model."""

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
    search_fields = (
        "name",
        "category__name",
    )
