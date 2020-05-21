from rest_framework import serializers
from rest_framework.fields import IntegerField

from billing.serializers import BillingProfileSerializer
from cart.serializers import CartSerializer

from .models import Order


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
