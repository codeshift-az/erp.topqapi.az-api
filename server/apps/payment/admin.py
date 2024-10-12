from django.contrib import admin

from server.apps.payment.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """Admin class for Payment model."""

    list_display = (
        "supplier",
        "amount",
        "date",
        "note",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "supplier",
        "date",
        "updated_at",
        "created_at",
    )
