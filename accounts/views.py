from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from order.models import Order
from order.serializers import DetailedOrderSerializer, OrderSerializer


class UserOrderList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        orders = Order.objects.filter(billing_profile__user=request.user).all()
        return Response(OrderSerializer(orders, many=True).data)


class OrderDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, order_id, **kwargs):
        order_obj: Order = get_object_or_404(Order, order_id=order_id)
        if order_obj.billing_profile.user != request.user:
            return Response(status=401)
        return Response(DetailedOrderSerializer(order_obj).data)
