from django.contrib import admin

from server.apps.staff.models import Driver, Worker


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    """Admin class for Worker model."""

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


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    """Admin class for Driver model."""

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
