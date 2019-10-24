from rest_framework import serializers
from rest_framework.fields import Field
from cart.models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        total = Field(source='total')
        total_cart_products = Field(source='total_cart_products')
        fields = ['id', 'user', 'products',
                  'used', 'total', 'total_cart_products']
