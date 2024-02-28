from rest_framework import serializers

from server.apps.supplier.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    """Serializer definition for Supplier model."""

    class Meta:
        """Meta definition for SupplierSerializer."""

        model = Supplier
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
