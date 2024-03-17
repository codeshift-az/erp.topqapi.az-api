from django.db import models

from server.apps.core.models import CoreModel


class OrderStatus(models.IntegerChoices):
    """Order status choices."""

    DRAFT = 0, "Sifariş qeydə alındı"
    REGISTERED = 1, "Sifariş qəbul olundu"
    ACCEPTED = 2, "Sifariş  hazırlanır"


class Order(CoreModel):
    """Model definition for Order."""

    branch = models.ForeignKey("branch.Branch", on_delete=models.CASCADE, related_name="orders")
    seller = models.ForeignKey("staff.Seller", on_delete=models.CASCADE, related_name="orders")

    customer = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    discount = models.PositiveSmallIntegerField(default=0)

    note = models.TextField(blank=True)

    status = models.PositiveSmallIntegerField(choices=OrderStatus.choices, default=OrderStatus.DRAFT)

    date = models.DateField()

    class Meta(CoreModel.Meta):
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        """Unicode representation of Order."""
        return f"Sifariş: #{self.id}"


class OrderItem(CoreModel):
    """Model definition for OrderItem."""

    order = models.ForeignKey("order.Order", on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, related_name="order_products")
    supplier = models.ForeignKey("supplier.Supplier", on_delete=models.CASCADE, related_name="order_products")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantity = models.PositiveSmallIntegerField(default=0)

    class Meta(CoreModel.Meta):
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"

    def __str__(self):
        """Unicode representation of OrderItem."""
        return f"Order Item: {self.product.name}"


class OrderCartItem(CoreModel):
    """Model definition for OrderCartItem."""

    user = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="order_cart")
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, related_name="order_cart")
    supplier = models.ForeignKey("supplier.Supplier", on_delete=models.CASCADE, related_name="order_cart")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantity = models.PositiveIntegerField(default=0)

    class Meta(CoreModel.Meta):
        verbose_name = "Order Cart Item"
        verbose_name_plural = "Order Cart Items"

    def __str__(self):
        """Unicode representation of OrderCartItem."""
        return f"{self.product.name}: {self.price} AZN - {self.quantity}x"
