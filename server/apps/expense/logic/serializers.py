from rest_framework import serializers

from server.apps.branch.logic.fields import BranchField
from server.apps.expense.models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    """Serializer definition for Expense model."""

    branch = BranchField()

    class Meta:
        model = Expense
        fields = (
            "id",
            "name",
            "branch",
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
