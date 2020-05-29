from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product

from .models import Cart, CartItem
from .serializers import CartSerializer


class CartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        cart_obj, _ = Cart.objects.get_existing_or_new(request)
        context = {'request': request}
        serializer = CartSerializer(cart_obj, context=context)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # Request Data
        product_id = request.data.get("id")
        quantity = int(request.data.get("quantity", 1))

        # Get Product Obj and Cart Obj
        product_obj = get_object_or_404(Product, pk=product_id)
        cart_obj, _ = Cart.objects.get_existing_or_new(request)

        if quantity <= 0:
            cart_item_qs = CartItem.objects.filter(
                cart=cart_obj, product=product_obj)
            if cart_item_qs.count != 0:
                cart_item_qs.first().delete()
        else:
            cart_item_obj, created = CartItem.objects.get_or_create(
                product=product_obj, cart=cart_obj)
            cart_item_obj.quantity = quantity
            cart_item_obj.save()

        serializer = CartSerializer(cart_obj, context={'request': request})
        return Response(serializer.data)


class CheckProductInCart(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, product_id, **kwargs):
        product_obj = get_object_or_404(Product, pk=product_id)
        cart_obj, created = Cart.objects.get_existing_or_new(request)
        return Response(not created and CartItem.objects.filter(cart=cart_obj, product=product_obj).exists())
