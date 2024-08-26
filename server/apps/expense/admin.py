from django.contrib import admin

from server.apps.expense.models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    """Admin class for Expense model."""

    list_display = (
        "name",
        "branch",
        "amount",
        "date",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "date",
        "updated_at",
        "created_at",
    )
    search_fields = ("name",)
