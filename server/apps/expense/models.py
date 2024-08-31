from django.db import models

from server.apps.core.models import TimeStampedModel


class Expense(TimeStampedModel):
    """Model definition for Expense."""

    name = models.CharField(max_length=255)
    branch = models.ForeignKey(
        "branch.Branch", on_delete=models.CASCADE, related_name="expenses", null=True, blank=True
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateField()

    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"

        ordering = ("-updated_at",)

    def __str__(self):
        """Unicode representation of Expense."""
        return f"{self.name}: {self.amount}"
