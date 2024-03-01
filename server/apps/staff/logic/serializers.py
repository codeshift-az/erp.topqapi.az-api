from rest_framework import serializers

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

    class Meta:
        model = Seller
        fields = (
            "id",
            "name",
            "branch",
            "salary",
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

    class Meta:
        model = Worker
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
