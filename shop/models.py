import os
import uuid

from django.db import models
from django.urls import reverse
from pytils.translit import slugify


def product_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.product.title)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/products/", filename)


class Category(models.Model):
    """
    Model responsible for category products.
    """

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        kwargs = {
            "category_slug": self.slug,
        }
        return reverse("category_detail", kwargs=kwargs)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Product(models.Model):
    """
    Model responsible for products
    """

    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True)
    price = models.IntegerField()
    description = models.TextField()
    size = models.PositiveIntegerField()
    materials = models.ManyToManyField("Material")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"product_slug": self.slug})

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["id"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Material(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materials"
        ordering = ["id"]


class ProductImage(models.Model):
    """
    Model responsible for product images
    """

    product = models.ForeignKey(
        Product, default=None, on_delete=models.CASCADE, related_name="product_images"
    )
    image = models.ImageField(
        null=True, blank=True, upload_to=product_image_file_path, max_length=255
    )

    def __str__(self):
        return self.product.title

    class Meta:
        ordering = ["-id"]
