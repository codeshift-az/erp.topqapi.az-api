from django.db import models

from server.apps.core.models import CoreModel


class FactoryProduct(CoreModel):
    """Model definition for FactoryProduct."""

    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey("category.Category", on_delete=models.CASCADE, related_name="factory_products")

    class Meta(CoreModel.Meta):
        verbose_name = "Factory Product"
        verbose_name_plural = "Factory Products"

    def __str__(self):
        """Unicode representation of FactoryProduct."""
        return f"Factory Product: {self.name}"
