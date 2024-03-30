from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from wishlist.models import Wishlist
from wishlist.serializers import WishlistSerializer


class WishlistViewSet(viewsets.ModelViewSet):
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Wishlist.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
