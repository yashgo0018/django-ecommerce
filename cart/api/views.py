from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import Cart
from products.models import Product

from .serializers import CartSerializer


class CartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        cart_obj = Cart.objects.get_existing_or_new(request)[0]
        serializer = CartSerializer(cart_obj)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get("id")
        product_obj = Product.objects.get(id=product_id)
        cart_obj = Cart.objects.get_existing_or_new(request)[0]
        if request.POST.get('type') == "remove":
            cart_obj.products.remove(product_obj)
            cart_obj.save()
        else:
            cart_obj.products.add(product_obj)
            cart_obj.save()
        serializer = CartSerializer(cart_obj)
        return Response(serializer.data)
