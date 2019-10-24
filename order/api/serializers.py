from rest_framework import serializers
from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'billing_profile',
            'order_id',
            'cart',
            'active',
            'status',
            'timestamp',
            'shipping_total',
            'total',
        ]
