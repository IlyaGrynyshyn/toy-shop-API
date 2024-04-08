from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from wishlist.models import Wishlist
from wishlist.serializers import WishlistSerializer


class WishlistViewSet(viewsets.ModelViewSet):
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Wishlist.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        product_id = serializer.validated_data.get("product")
        existing_wishlist = Wishlist.objects.filter(
            owner=self.request.user, product_id=product_id
        )
        if existing_wishlist:
            return Response(
                {"error": "This product is already in your wishlist."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        product_id = self.kwargs["pk"]
        print(kwargs)
        try:
            wishlist_item = Wishlist.objects.get(
                owner=self.request.user, product_id=product_id
            )
            self.perform_destroy(wishlist_item)
        except Wishlist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
