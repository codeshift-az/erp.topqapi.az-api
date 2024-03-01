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


class Seller(CoreModel):
    """Model definition for Seller."""

    name = models.CharField(max_length=255, unique=True)
    branch = models.ForeignKey("branch.Branch", on_delete=models.CASCADE, related_name="sellers")
    salary = models.PositiveIntegerField(default=0)

    class Meta(CoreModel.Meta):
        verbose_name = "Seller"
        verbose_name_plural = "Sellers"

    def __str__(self):
        """Unicode representation of Seller."""
        return f"{self.name} - {self.branch.name}"


class Worker(CoreModel):
    """Model definition for Worker."""

    name = models.CharField(max_length=255, unique=True)

    class Meta(CoreModel.Meta):
        verbose_name = "Worker"
        verbose_name_plural = "Workers"

    def __str__(self):
        """Unicode representation of Worker."""
        return self.name
