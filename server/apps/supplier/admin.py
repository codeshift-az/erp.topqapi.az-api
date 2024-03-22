from django.contrib import admin

from server.apps.supplier.models import Supplier, SupplierPayment


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """Admin class for Supplier model."""

    list_display = (
        "name",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "updated_at",
        "created_at",
    )
    search_fields = ("name",)


@admin.register(SupplierPayment)
class SupplierPaymentAdmin(admin.ModelAdmin):
    """Admin class for SupplierPayment model."""

    list_display = (
        "supplier",
        "amount",
        "date",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "supplier",
        "updated_at",
        "created_at",
    )
