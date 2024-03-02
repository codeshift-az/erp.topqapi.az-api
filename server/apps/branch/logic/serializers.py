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

    def __init__(self, *args, **kwargs):
        """Override the __init__ method."""

        super().__init__(*args, **kwargs)

        if self.instance is not None:
            for field in self.fields:
                self.fields[field].required = False
