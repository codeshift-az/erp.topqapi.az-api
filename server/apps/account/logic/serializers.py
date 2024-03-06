from rest_framework import serializers

from server.apps.user.models import User


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
