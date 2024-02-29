from rest_framework import serializers

from shop.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "title", "slug", "price")
        model = Product
        lookup_field = "slug"
