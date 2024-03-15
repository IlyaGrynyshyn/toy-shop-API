from rest_framework import viewsets

from order.models import Order
from order.serializers import OrderSerializer
from shop.permissions import IsAdminUserOrReadOnly


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUserOrReadOnly]


    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
