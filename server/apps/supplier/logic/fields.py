from rest_framework import serializers

import server.apps.supplier.logic.schema  # noqa: F401
from server.apps.supplier.logic.serializers import SupplierSerializer
from server.apps.supplier.models import Supplier


class SupplierField(serializers.RelatedField):
    """Serializer definition for Supplier field."""

    def get_queryset(self):
        """Return queryset of Supplier objects."""
        return Supplier.objects.all()

    def to_representation(self, value: Supplier) -> dict:
        """Return representation of Supplier object."""
        return SupplierSerializer(value).data

    def to_internal_value(self, data: int) -> Supplier:
        """Return Supplier object from given data."""
        supplier = Supplier.objects.get(pk=data)

        if supplier is None:
            return serializers.ValidationError(f"Supplier with id {data} does not exist.")

        return supplier
