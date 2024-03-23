from rest_framework import serializers

from server.apps.factory.product.logic.fields import FactoryProductField
from server.apps.factory.storage.models import FactoryStorageItem
from server.apps.factory.usage.models import FactoryUsage


class FactoryUsageSerializer(serializers.ModelSerializer):
    """Serializer definition for FactoryUsage model."""

    product = FactoryProductField()

    class Meta:
        model = FactoryUsage
        fields = (
            "id",
            "product",
            "quantity",
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

        usage = super().create(validated_data)

        count = usage.quantity
        n = 0

        while count > 0:
            usage.items.create(
                usage=usage,
                storage=items[n],
                quantity=count if items[n].left >= count else items[n].left,
            )
            count -= items[n].left
            n += 1

        return usage

    def update(self, instance, validated_data):
        quantity = validated_data.get("quantity", None)
        product = validated_data.get("product", None)

        items = (
            FactoryStorageItem.objects.get_related()
            .get_sales()
            .filter(product=product if product else instance.product, left__gt=0)
        )

        if quantity and (sum([item.left for item in items]) + (instance.quantity if product else 0) < quantity):
            raise serializers.ValidationError({"quantity": "Istehsalat anbarında bu məhsuldan yetərli qədər yoxdur!"})

        usage = super().update(instance, validated_data)

        if quantity is None and product is None:
            return usage

        for item in usage.items.all():
            item.delete()

        count = usage.quantity
        n = 0

        items = list(FactoryStorageItem.objects.get_related().get_sales().filter(product=usage.product, left__gt=0))

        while count > 0:
            usage.items.create(
                usage=usage,
                storage=items[n],
                quantity=count if items[n].left >= count else items[n].left,
            )
            count -= items[n].left
            n += 1

        return usage
