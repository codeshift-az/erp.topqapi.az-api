from rest_framework import serializers

from server.apps.payment.models import Payment
from server.apps.supplier.logic.fields import SupplierField


class PaymentSerializer(serializers.ModelSerializer):
    """Serializer definition for Payment model."""

    supplier = SupplierField()

    class Meta:
        model = Payment
        fields = (
            "id",
            "supplier",
            "amount",
            "date",
            "note",
            "updated_at",
            "created_at",
        )
        read_only_fields = (
            "id",
            "updated_at",
            "created_at",
        )
