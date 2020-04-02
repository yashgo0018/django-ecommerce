from rest_framework import serializers
from rest_framework.fields import IntegerField
from order.models import Order
from billing.api.serializers import BillingProfileSerializer
from cart.api.serializers import CartSerializer


class OrderSerializer(serializers.ModelSerializer):
    billing_profile = BillingProfileSerializer()
    cart = CartSerializer()

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
            'total_in_paise',
        ]

        total_in_paise = IntegerField(source='total_in_paise')
