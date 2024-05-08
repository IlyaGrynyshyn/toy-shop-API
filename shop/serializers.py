from rest_framework import serializers

from shop.models import Product, Category, ProductImage, Material


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Category
        fields = ("id", "title", "slug")


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = (
            "id",
            "name",
        )


class ProductMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ("name",)


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
    size = serializers.IntegerField(write_only=True)
    description = serializers.CharField(read_only=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "category",
            "images",
            "slug",
            "price",
            "size",
            "description",
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
    size = serializers.IntegerField()
    materials = ProductMaterialSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "category",
            "slug",
            "price",
            "description",
            "size",
            "materials",
            "images",
        )
