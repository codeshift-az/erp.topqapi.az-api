from django.db import models

from server.apps.core.models import CoreModel


class Entry(CoreModel):
    """Model definition for Entry."""

    supplier = models.ForeignKey("supplier.Supplier", on_delete=models.CASCADE, related_name="entries")
    invoice = models.CharField(max_length=255, blank=True)
    date = models.DateField()

    class Meta(CoreModel.Meta):
        verbose_name = "Entry"
        verbose_name_plural = "Entries"

    def __str__(self):
        """Unicode representation of Entry."""
        return f"Entry: #{self.pk} - {self.date}"


class Product(CoreModel):
    """Model definition for Product."""

    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name="products")
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, related_name="warehouse")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)

    class Meta(CoreModel.Meta):
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        """Unicode representation of Product."""
        return f"Product: {self.product.name}"


class CartItem(CoreModel):
    """Model definition for CartItem."""

    user = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="warehouse_cart")
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, related_name="warehouse_cart")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantity = models.PositiveIntegerField(default=0)

    class Meta(CoreModel.Meta):
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"

    def __str__(self):
        """Unicode representation of CartItem."""
        return f"{self.product.name}: {self.price} AZN - {self.quantity}x"
