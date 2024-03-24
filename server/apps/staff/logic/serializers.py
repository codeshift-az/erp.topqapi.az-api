from rest_framework import serializers

from server.apps.branch.logic.fields import BranchField
from server.apps.staff.models import Driver, Seller, Worker


class DriverSerializer(serializers.ModelSerializer):
    """Serializer definition for Driver model."""

    current_month_orders = serializers.IntegerField(read_only=True)
    past_month_orders = serializers.IntegerField(read_only=True)

    class Meta:
        model = Driver
        fields = (
            "id",
            "name",
            "current_month_orders",
            "past_month_orders",
            "updated_at",
            "created_at",
        )
        read_only_fields = (
            "id",
            "updated_at",
            "created_at",
        )


class SellerSerializer(serializers.ModelSerializer):
    """Serializer definition for Seller model."""

    branch = BranchField()

    current_month_orders = serializers.IntegerField(read_only=True)
    past_month_orders = serializers.IntegerField(read_only=True)

    current_month_share = serializers.IntegerField(read_only=True)
    past_month_share = serializers.IntegerField(read_only=True)

    class Meta:
        model = Seller
        fields = (
            "id",
            "name",
            "branch",
            "salary",
            "current_month_orders",
            "past_month_orders",
            "current_month_share",
            "past_month_share",
            "updated_at",
            "created_at",
        )
        read_only_fields = (
            "id",
            "updated_at",
            "created_at",
        )


class WorkerSerializer(serializers.ModelSerializer):
    """Serializer definition for Worker model."""

    current_month_orders = serializers.IntegerField(read_only=True)
    past_month_orders = serializers.IntegerField(read_only=True)

    class Meta:
        model = Worker
        fields = (
            "id",
            "name",
            "current_month_orders",
            "past_month_orders",
            "updated_at",
            "created_at",
        )
        read_only_fields = (
            "id",
            "updated_at",
            "created_at",
        )
