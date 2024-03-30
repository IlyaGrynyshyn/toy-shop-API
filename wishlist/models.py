from django.db import models
from customer.models import Customer
from shop.models import Product


class Wishlist(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.owner} - {self.product}"
