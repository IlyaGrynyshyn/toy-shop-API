from django.db import transaction
from rest_framework import serializers

from order.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("id", "product", "quantity", "price")


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    total_price = serializers.SerializerMethodField()
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ("id", "order_items", "total_price", "total_amount", "created_at")

    def get_total_price(self, obj):
        """Get total price of order."""
        total_price = 0
        for order_item in obj.order_items.all():
            total_price += order_item.price * order_item.quantity
        return total_price

    def get_total_amount(self, obj):
        """Get total amount of order."""
        total_amount = 0
        for order_item in obj.order_items.all():
            total_amount += order_item.quantity
        return total_amount

    @transaction.atomic()
    def create(self, validated_data):
        order_items_data = validated_data.pop("order_items")
        order = Order.objects.create(**validated_data)
        for order_item in order_items_data:
            OrderItem.objects.create(order=order, **order_item)
        return order
