from django.db import models


class OrderStatus(models.IntegerChoices):
    """Order status choices."""

    DRAFT = 0, "DRAFT"
    REGISTERED = 1, "Satış qeydə alındı"
    ACCEPTED = 2, "Anbar satışı qəbul etdi"
    PENDING = 3, "Məhsullar hazırlanır"
    READY = 4, "Məhsullar hazırdır"
    RETURN = 5, "Geri Qayıtma"
    ON_DELIVERY = 6, "Məhsullar yoldadır"
    DELIVERED = 7, "Məhsullar çatdırıldı"
    INSTALLED = 8, "Satış tamamlandı"
