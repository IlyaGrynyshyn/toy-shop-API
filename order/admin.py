from django.contrib import admin
from order.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["product"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "created_at",
    ]
    list_filter = ["user", "created_at"]
    search_fields = ["user", "created_at"]
    inlines = [OrderItemInline]
