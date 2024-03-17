from django.db import models

from server.apps.core.models import CoreModel


class WarehouseEntry(CoreModel):
    """Model definition for WarehouseEntry."""

    supplier = models.ForeignKey("supplier.Supplier", on_delete=models.CASCADE, related_name="entries")
    invoice = models.CharField(max_length=255, blank=True)
    date = models.DateField()

    class Meta(CoreModel.Meta):
        verbose_name = "Warehouse Entry"
        verbose_name_plural = "Warehouse Entries"

    def __str__(self):
        """Unicode representation of WarehouseEntry."""
        return f"Warehouse Entry: #{self.pk} - {self.date}"


class WarehouseItem(CoreModel):
    """Model definition for WarehouseItem."""

    entry = models.ForeignKey(WarehouseEntry, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, related_name="warehouse_items")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)

    class Meta(CoreModel.Meta):
        verbose_name = "WarehouseItem"
        verbose_name_plural = "WarehouseItems"

    def __str__(self):
        """Unicode representation of WarehouseItem."""
        return f"WarehouseItem: {self.product.name}"


class WarehouseCartItem(CoreModel):
    """Model definition for WarehouseCartItem."""

    user = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="warehouse_cart")
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, related_name="warehouse_cart")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantity = models.PositiveIntegerField(default=0)

    class Meta(CoreModel.Meta):
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"

    def __str__(self):
        """Unicode representation of WarehouseCartItem."""
        return f"{self.product.name}: {self.price} AZN - {self.quantity}x"
