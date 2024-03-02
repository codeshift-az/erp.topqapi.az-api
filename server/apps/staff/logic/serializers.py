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

    def __init__(self, *args, **kwargs):
        """Override the __init__ method."""

        super().__init__(*args, **kwargs)

        if self.instance is not None:
            for field in self.fields:
                self.fields[field].required = False


class SellerSerializer(serializers.ModelSerializer):
    """Serializer definition for Seller model."""

    branch = BranchField()

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

    def __init__(self, *args, **kwargs):
        """Override the __init__ method."""

        super().__init__(*args, **kwargs)

        if self.instance is not None:
            for field in self.fields:
                self.fields[field].required = False


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

    def __init__(self, *args, **kwargs):
        """Override the __init__ method."""

        super().__init__(*args, **kwargs)

        if self.instance is not None:
            for field in self.fields:
                self.fields[field].required = False
