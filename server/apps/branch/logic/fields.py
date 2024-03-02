from rest_framework import serializers

import server.apps.branch.logic.schema  # noqa: F401
from server.apps.branch.logic.serializers import BranchSerializer
from server.apps.branch.models import Branch


class BranchField(serializers.RelatedField):
    """Serializer definition for Branch field."""

    def get_queryset(self):
        """Return queryset of Branch objects."""
        return Branch.objects.all()

    def to_representation(self, value: Branch) -> dict:
        """Return representation of Branch object."""
        return BranchSerializer(value).data

    def to_internal_value(self, data: int) -> Branch:
        """Return Branch object from given data."""
        branch = Branch.objects.get(pk=data)

        if branch is None:
            return serializers.ValidationError(f"Branch with id {data} does not exist.")

        return branch
