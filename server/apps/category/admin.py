from django.contrib import admin

from server.apps.category.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin class for Category model."""

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
