from rest_framework import serializers

from shop.models import Product


class ProductSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        fields = ("id", "title", "slug", "price", "image")
        model = Product
        lookup_field = "slug"


class ProdcuctListSerializer(ProductSerializer): ...


class ProdcutDetailSerializer(ProductSerializer): ...


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "image")
