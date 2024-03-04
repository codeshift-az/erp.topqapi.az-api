from django.db import models

from server.apps.core.models import CoreModel


class Branch(CoreModel):
    """Model definition for Branch."""

    name = models.CharField(max_length=255, unique=True)
    user = models.OneToOneField("user.User", on_delete=models.CASCADE, related_name="branch")

    class Meta(CoreModel.Meta):
        verbose_name = "Branch"
        verbose_name_plural = "Branches"

    def __str__(self):
        """Unicode representation of Branch."""
        return self.name

    def delete(self):
        """Delete user object when branch is deleted."""
        self.user.delete()
        super().delete()
