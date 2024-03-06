from django.contrib import admin

from server.apps.warehouse.models import Entry, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin class for Product model."""

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


class ProductInline(admin.TabularInline):
    """Admin Inline class for Product Model."""

    model = Product
    extra = 1


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    """Admin class for Entry model."""

    inlines = (ProductInline,)

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
