from django.contrib import admin

from server.apps.staff.models import Driver, Seller, Worker


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


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    """Admin class for Seller model."""

    list_display = (
        "name",
        "branch",
        "salary",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "branch",
        "updated_at",
        "created_at",
    )
    search_fields = (
        "name",
        "branch",
    )


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
