from rest_framework import serializers

from shop.models import Product, Category, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Category
        fields = ("id", "title", "slug")


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ("image",)


class ProductSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True, source="product_images")
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(
            max_length=1000000, allow_empty_file=False, use_url=False
        ),
        write_only=True,
    )

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "category",
            "images",
            "slug",
            "price",
            "uploaded_images",
        )

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        product = Product.objects.create(**validated_data)
        for image in uploaded_images:
            ProductImage.objects.create(product=product, image=image)
        return product


class ProductDetailSerializer(ProductSerializer):
    category = CategorySerializer()
