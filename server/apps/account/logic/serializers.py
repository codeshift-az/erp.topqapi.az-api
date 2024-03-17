from rest_framework import serializers

from server.apps.branch.logic.serializers import BranchSerializer
from server.apps.user.models import User, UserTypes


class AccountSerializer(serializers.ModelSerializer):
    """Serializer for Account model."""

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "type",
            "is_active",
            "is_staff",
            "is_superuser",
            "date_joined",
        )
        extra_kwargs = {
            "first_name": {"required": False},
            "last_name": {"required": False},
            "username": {"required": False},
            "email": {"required": False},
        }
        read_only_fields = ("is_active", "is_staff", "is_superuser", "date_joined")

    def to_representation(self, instance):
        """Return representation of Account model."""
        data = super().to_representation(instance)

        if instance.type == UserTypes.STORE:
            data["branch"] = BranchSerializer(instance.branch).data

        return data
