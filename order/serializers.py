import string
import random

from django.db import transaction
from rest_framework import serializers

from order.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("id", "product", "price")


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    total_price = serializers.SerializerMethodField()
    track_number = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            "id",
            "order_items",
            "first_name",
            "last_name",
            "middle_name",
            "phone_number",
            "delivery_city",
            "delivery_warehouse",
            "total_price",
            "track_number",
            "created_at",
        )

    def get_total_price(self, obj):
        """Get total price of order."""
        total_price = 0
        for order_item in obj.order_items.all():
            total_price += order_item.price
        return total_price

    def get_track_number(self, obj):
        """It's just a plug for field track number"""
        available_characters = string.digits
        tracking_number = "".join(
            random.choice(available_characters) for _ in range(16)
        )

        return tracking_number

    @transaction.atomic()
    def create(self, validated_data):
        order_items_data = validated_data.pop("order_items")
        order = Order.objects.create(**validated_data)
        for order_item in order_items_data:
            OrderItem.objects.create(order=order, **order_item)
        return order
