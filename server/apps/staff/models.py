from django.db import models

from server.apps.core.models import TimeStampedModel

# Model Queryset
from server.apps.staff.logic.queryset import DriverQuerySet, SellerQuerySet, WorkerQuerySet


class Driver(TimeStampedModel):
    """Model definition for Driver."""

    name = models.CharField(max_length=255, unique=True)

    objects = DriverQuerySet.as_manager()

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"

        ordering = ("-updated_at",)

    def __str__(self):
        """Unicode representation of Driver."""
        return self.name


class Seller(TimeStampedModel):
    """Model definition for Seller."""

    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    branch = models.ForeignKey("branch.Branch", on_delete=models.CASCADE, related_name="sellers")
    salary = models.PositiveIntegerField(default=0)

    objects = SellerQuerySet.as_manager()

    class Meta:
        verbose_name = "Seller"
        verbose_name_plural = "Sellers"

        ordering = ("-updated_at",)

    def __str__(self):
        """Unicode representation of Seller."""
        return f"{self.name} - {self.branch.name}"


class Worker(TimeStampedModel):
    """Model definition for Worker."""

    name = models.CharField(max_length=255, unique=True)

    objects = WorkerQuerySet.as_manager()

    class Meta:
        verbose_name = "Worker"
        verbose_name_plural = "Workers"

        ordering = ("-updated_at",)

    def __str__(self):
        """Unicode representation of Worker."""
        return self.name
