from rest_framework import serializers

from server.apps.category.logic.fields import CategoryField
from server.apps.product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Serializer definition for Product model."""

    category = CategoryField()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "category",
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
