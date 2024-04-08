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

    class Meta:
        model = Order
        fields = (
            "id",
            "order_items",
            "delivery_city",
            "delivery_warehouse",
            "total_price",
            "created_at",
        )

    def get_total_price(self, obj):
        """Get total price of order."""
        total_price = 0
        for order_item in obj.order_items.all():
            total_price += order_item.price
        return total_price

    @transaction.atomic()
    def create(self, validated_data):
        order_items_data = validated_data.pop("order_items")
        order = Order.objects.create(**validated_data)
        for order_item in order_items_data:
            OrderItem.objects.create(order=order, **order_item)
        return order
