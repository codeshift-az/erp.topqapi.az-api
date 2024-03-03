from rest_framework import serializers

from server.apps.expense.models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    """Serializer definition for Expense model."""

    class Meta:
        model = Expense
        fields = (
            "id",
            "name",
            "amount",
            "date",
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
