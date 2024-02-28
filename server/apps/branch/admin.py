from django.contrib import admin

from server.apps.branch.models import Branch


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    """Admin definition for Branch model."""

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
