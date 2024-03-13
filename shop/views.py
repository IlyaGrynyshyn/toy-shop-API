from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


from shop.models import Product, Category, ProductImage
from shop.permissions import IsAdminUserOrReadOnly
from shop.serializers import (
    ProductSerializer,
    ProductDetailSerializer,
    ProductImageSerializer,
    CategorySerializer,
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

    @action(
        methods=["POST"],
        detail=True,
        url_path="upload-image",
        permission_classes=[IsAdminUser],
    )
    def upload_image(self, request, slug=None):
        """Endpoint for uploading image to specific product"""
        products = self.get_object()
        serializer = self.get_serializer(products, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
