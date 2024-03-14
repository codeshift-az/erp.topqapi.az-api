from rest_framework import serializers

import server.apps.staff.logic.schema  # noqa: F401
from server.apps.staff.logic.serializers import SellerSerializer
from server.apps.staff.models import Seller


class SellerField(serializers.RelatedField):
    """Serializer definition for Seller field."""

    def get_queryset(self):
        """Return queryset of Seller objects."""
        return Seller.objects.all()

    def to_representation(self, value: Seller) -> dict:
        """Return representation of Seller object."""
        return SellerSerializer(value).data

    def to_internal_value(self, data: int) -> Seller:
        """Return Seller object from given data."""
        seller = Seller.objects.get(pk=data)

        if seller is None:
            return serializers.ValidationError(f"Seller with id {data} does not exist.")

        return seller
