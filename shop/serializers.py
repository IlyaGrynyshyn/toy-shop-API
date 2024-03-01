from rest_framework import serializers

from shop.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Category
        fields = ("id", "title", "slug")
        lookup_field = "slug"


class ProductSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        fields = ("id", "title", "category", "slug", "price", "image")
        model = Product
        lookup_field = "slug"


class ProdcutDetailSerializer(ProductSerializer):
    category = CategorySerializer()


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "image")
