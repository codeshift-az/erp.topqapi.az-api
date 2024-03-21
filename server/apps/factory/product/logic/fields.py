from rest_framework import serializers

import server.apps.factory.product.logic.schema  # noqa: F401
from server.apps.factory.product.logic.serializers import FactoryProductSerializer
from server.apps.factory.product.models import FactoryProduct


class FactoryProductField(serializers.RelatedField):
    """Serializer definition for FactoryProduct field."""

    def get_queryset(self):
        """Return queryset of FactoryProduct objects."""
        return FactoryProduct.objects.all()

    def to_representation(self, value: FactoryProduct) -> dict:
        """Return representation of FactoryProduct object."""
        return FactoryProductSerializer(value).data

    def to_internal_value(self, data: int) -> FactoryProduct:
        """Return FactoryProduct object from given data."""
        factory_product = FactoryProduct.objects.get(pk=data)

        if factory_product is None:
            return serializers.ValidationError(f"FactoryProduct with id {data} does not exist.")

        return factory_product
