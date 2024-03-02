from rest_framework import serializers

from server.apps.supplier.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    """Serializer definition for Supplier model."""

    class Meta:
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

    def __init__(self, *args, **kwargs):
        """Override the __init__ method."""

        super().__init__(*args, **kwargs)

        if self.instance is not None:
            for field in self.fields:
                self.fields[field].required = False
