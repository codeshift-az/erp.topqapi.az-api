from rest_framework import serializers

from server.apps.factory.product.logic.fields import FactoryProductField
from server.apps.factory.sale.models import FactorySale
from server.apps.factory.storage.models import FactoryStorageItem


class FactorySaleSerializer(serializers.ModelSerializer):
    """Serializer definition for FactorySale model."""

    product = FactoryProductField()

    class Meta:
        model = FactorySale
        fields = (
            "id",
            "product",
            "quantity",
            "price",
            "date",
            "updated_at",
            "created_at",
        )
        read_only_fields = (
            "id",
            "updated_at",
            "created_at",
        )

    def create(self, validated_data):
        items = FactoryStorageItem.objects.filter(product=validated_data["product"]).get_related().get_sales()

        if sum([item.left for item in items]) < validated_data["quantity"]:
            raise serializers.ValidationError({"quantity": "Istehsalat anbarında bu məhsuldan yetərli qədər yoxdur!"})

        sale = super().create(validated_data)

        count = sale.quantity
        n = 0

        while count > 0:
            sale.items.create(
                sale=self.instance,
                storage=items[n],
                quantity=count if items[n].left >= count else items[n].left,
            )
            count -= items[n].left
            n += 1

        return sale
