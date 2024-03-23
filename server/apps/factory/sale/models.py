from django.db import models

from server.apps.core.models import CoreModel


class FactorySale(CoreModel):
    """Model definition for FactorySale."""

    product = models.ForeignKey("factory_product.FactoryProduct", on_delete=models.CASCADE, related_name="sales")
    quantity = models.PositiveSmallIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date = models.DateField()

    class Meta(CoreModel.Meta):
        verbose_name = "Factory Salem"
        verbose_name_plural = "Factory Salems"

    def __str__(self):
        """Unicode representation of FactorySale."""
        return f"Factory Salem: {self.name}"


class FactorySaleItem(CoreModel):
    """Model definition for FactorySaleItem."""

    sale = models.ForeignKey(FactorySale, on_delete=models.CASCADE, related_name="items")
    storage = models.ForeignKey("factory_storage.FactoryStorageItem", on_delete=models.CASCADE, related_name="sales")
    quantity = models.PositiveIntegerField()

    class Meta(CoreModel.Meta):
        verbose_name = "FactorySaleItem"
        verbose_name_plural = "FactorySaleItems"

    def __str__(self):
        """Unicode representation of FactorySaleItem."""
        return f"{self.sale.product.name}"
