from django.db import models

from server.apps.core.models import CoreModel


class Expense(CoreModel):
    """Model definition for Expense."""

    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateField()

    class Meta(CoreModel.Meta):
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"

    def __str__(self):
        """Unicode representation of Expense."""
        return f"{self.name}: {self.amount}"
