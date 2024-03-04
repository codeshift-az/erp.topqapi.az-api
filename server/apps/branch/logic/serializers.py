from rest_framework import serializers

from server.apps.branch.models import Branch


class BranchSerializer(serializers.ModelSerializer):
    """Serializer definition for Branch model."""

    class Meta:
        model = Branch
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
