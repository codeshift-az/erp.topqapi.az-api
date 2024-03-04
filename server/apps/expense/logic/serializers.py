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
