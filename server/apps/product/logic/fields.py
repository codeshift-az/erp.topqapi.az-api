from rest_framework import serializers

import server.apps.product.logic.schema  # noqa: F401
from server.apps.product.logic.serializers import ProductSerializer
from server.apps.product.models import Product


class ProductField(serializers.RelatedField):
    """Serializer definition for Product field."""

    def get_queryset(self):
        """Return queryset of Product objects."""
        return Product.objects.all()

    def to_representation(self, value: Product) -> dict:
        """Return representation of Product object."""
        return ProductSerializer(value).data

    def to_internal_value(self, data: int) -> Product:
        """Return Product object from given data."""
        product = Product.objects.get(pk=data)

        if product is None:
            return serializers.ValidationError(f"Product with id {data} does not exist.")

        return product
