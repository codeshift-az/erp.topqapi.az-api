from rest_framework import serializers

from server.apps.supplier.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    """Serializer definition for Supplier model."""

    total_price = serializers.IntegerField(read_only=True)
    total_payed = serializers.IntegerField(read_only=True)

    class Meta:
        model = Supplier
        fields = (
            "id",
            "name",
            "total_price",
            "total_payed",
            "updated_at",
            "created_at",
        )
        read_only_fields = (
            "id",
            "updated_at",
            "created_at",
        )
