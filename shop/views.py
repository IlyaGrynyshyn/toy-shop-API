from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets


from shop.models import Product, Category, ProductImage, Material
from shop.permissions import IsAdminUserOrReadOnly
from shop.serializers import (
    ProductSerializer,
    ProductDetailSerializer,
    ProductImageSerializer,
    CategorySerializer,
    MaterialSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_queryset(self):
        queryset = Product.objects.all()
        sort_by_price = self.request.query_params.get("sort")
        if sort_by_price == "price_asc":
            queryset = queryset.order_by("price")  # sort by price down from 1-10
        if sort_by_price == "price_desc":
            queryset = queryset.order_by("-price")  # sort by price from 10-1
        return queryset

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ProductDetailSerializer
        if self.action == "upload_image":
            return ProductImageSerializer
        return self.serializer_class

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "sort",
                type={"type": "string", "items": {"type": "text"}},
                description="Sort by price down use 'price_desc'. Sort by price up use 'price_asc' ",
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class MaterialsViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAdminUserOrReadOnly]
