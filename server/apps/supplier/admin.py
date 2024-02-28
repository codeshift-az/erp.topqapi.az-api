from django.contrib import admin

from server.apps.supplier.models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """Admin class for Supplier model."""

    list_display = ("name", "updated_at", "created_at")
    list_filter = ("updated_at", "created_at")
    search_fields = ("name",)
