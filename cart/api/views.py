from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import Cart
from products.models import Product

from .serializers import CartSerializer


class CartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        cart_obj, _ = Cart.objects.get_existing_or_new(request)
        context = {'request': request}
        serializer = CartSerializer(cart_obj, context=context)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # Get The Product Obj
        product_id = request.data.get("id")
        product_obj = get_object_or_404(Product, pk=product_id)

        # Get The Cart Obj
        cart_obj, _ = Cart.objects.get_existing_or_new(request)

        # Check Whether to remove the product or To add it
        if request.data.get('type') == "remove":
            cart_obj.products.remove(product_obj)
            cart_obj.save()
        elif request.data.get('type') == "add":
            cart_obj.products.add(product_obj)
            cart_obj.save()
        else:
            return Response({}, status=400)

        context = {'request': request}
        # Return The Cart Obj
        serializer = CartSerializer(cart_obj, context=context)
        return Response(serializer.data)
