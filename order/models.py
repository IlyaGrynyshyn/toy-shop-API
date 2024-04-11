from django.db import models
from django.conf import settings

from shop.models import Product


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_city = models.CharField(max_length=100)
    delivery_warehouse = models.CharField(max_length=100)
    track_number = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.email} - {self.created_at}"

    class Meta:
        ordering = ["-created_at"]


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_items"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "{}".format(self.id)
