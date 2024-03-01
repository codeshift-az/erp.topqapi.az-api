from django.db import models

from server.apps.core.models import CoreModel


class Driver(CoreModel):
    """Model definition for Driver."""

    name = models.CharField(max_length=255, unique=True)

    class Meta(CoreModel.Meta):
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"

    def __str__(self):
        """Unicode representation of Driver."""
        return self.name
