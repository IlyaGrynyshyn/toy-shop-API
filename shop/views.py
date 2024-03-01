from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


from shop.models import Product, Category
from shop.permissions import IsAdminUserOrReadOnly
from shop.serializers import (
    ProductSerializer,
    ProdcutDetailSerializer,
    ProductImageSerializer,
    CategorySerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]
    lookup_field = "slug"


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminUserOrReadOnly]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ProdcutDetailSerializer
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
