from django.db import models

from server.apps.core.models import TimeStampedModel


class Product(TimeStampedModel):
    """Model definition for Product."""

    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey("category.Category", on_delete=models.CASCADE, related_name="products")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

        ordering = ("-updated_at",)

    def __str__(self):
        """Unicode representation of Product."""
        return self.name
