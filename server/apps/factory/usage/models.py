from django.db import models

from server.apps.core.models import CoreModel


class FactoryUsage(CoreModel):
    """Model definition for FactoryUsage."""

    product = models.ForeignKey("factory_product.FactoryProduct", on_delete=models.CASCADE, related_name="usages")
    quantity = models.PositiveSmallIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date = models.DateField()

    class Meta(CoreModel.Meta):
        verbose_name = "Factory Usagem"
        verbose_name_plural = "Factory Usagems"

    def __str__(self):
        """Unicode representation of FactoryUsage."""
        return f"Factory Usagem: {self.name}"


class FactoryUsageItem(CoreModel):
    """Model definition for FactoryUsageItem."""

    usage = models.ForeignKey(FactoryUsage, on_delete=models.CASCADE, related_name="items")
    storage = models.ForeignKey("factory_storage.FactoryStorageItem", on_delete=models.CASCADE, related_name="usages")
    quantity = models.PositiveIntegerField()

    class Meta(CoreModel.Meta):
        verbose_name = "FactoryUsageItem"
        verbose_name_plural = "FactoryUsageItems"

    def __str__(self):
        """Unicode representation of FactoryUsageItem."""
        return f"{self.usage.product.name}"
