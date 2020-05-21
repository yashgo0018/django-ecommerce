from rest_framework import serializers
from rest_framework.fields import Field
from cart.models import Cart, CartItem
from products.api.serializers import ProductSerializer
from accounts.api.serializers import UserSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    products = CartItemSerializer(read_only=True, many=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Cart
        total = Field(source='total')
        total_cart_products = Field(source='total_cart_products')
        fields = ['id', 'user', 'products', 'total', 'total_cart_products']


# class CollegeDetailsSerializer(serializers.Serializer):
#     students = serializers.SerializerMethodField('get_students')
#     branches = serializers.SerializerMethodField('get_branches')

#     def __init__(self, *args, **kwargs):
#         context = kwargs.pop("context")
#         self.college_id = context.get('college_id')
#         super(CollegeDetailsSerializer, self).__init__(*args, **kwargs)

#     def get_students(self, obj):
#         return StudentSerializer(
#                     Student.objects.filter(college_id=self.college_id),
#                     many=True
#                 ).data

#     def get_branches(self, obj):
#         return BranchSerializer(
#                     Branch.objects.filter(college_id=self.college_id),
#                     many=True
#                 ).data
