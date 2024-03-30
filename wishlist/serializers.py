from rest_framework import serializers

from wishlist.models import Wishlist


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "product")
        model = Wishlist
