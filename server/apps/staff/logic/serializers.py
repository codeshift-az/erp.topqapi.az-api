from rest_framework import serializers

from server.apps.branch.logic.fields import BranchField
from server.apps.staff.models import Driver, Seller, Worker


class DriverSerializer(serializers.ModelSerializer):
    """Serializer definition for Driver model."""

    class Meta:
        model = Driver
        fields = (
            "id",
            "name",
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

    total_orders = serializers.IntegerField(read_only=True)
    total_share = serializers.IntegerField(read_only=True)

    class Meta:
        model = Seller
        fields = (
            "id",
            "name",
            "branch",
            "salary",
            "total_orders",
            "total_share",
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

    total_orders = serializers.IntegerField(read_only=True)

    class Meta:
        model = Worker
        fields = (
            "id",
            "name",
            "total_orders",
            "updated_at",
            "created_at",
        )
        read_only_fields = (
            "id",
            "updated_at",
            "created_at",
        )
