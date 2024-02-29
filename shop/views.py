from rest_framework import viewsets

from shop.models import Product
from shop.permissions import IsAdminUserOrReadOnly
from shop.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminUserOrReadOnly]
