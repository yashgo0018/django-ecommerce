import razorpay
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from billing.models import BillingProfile
from cart.models import Cart
from order.models import Order
from products.models import Product

from .serializers import OrderSerializer

razorpay_client = razorpay.Client(
    auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))


class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        profile_id = request.GET.get("profile_id")

        if profile_id == None:
            return Response({'error': 'Profile Id Not Found'}, status=400)

        profiles = BillingProfile.objects.filter(id=profile_id)

        if not profiles.count() == 1:
            return Response({'error': 'Profile Doesn\'t exist'}, status=400)

        cart_obj, new_obj = Cart.objects.get_existing_or_new(request)

        if cart_obj.total_cart_products() == 0:
            return Response({'error': 'Cart Is Empty'}, status=400)

        return Response({
            "order": OrderSerializer(self.get_order(profiles.first()), context={'request': request}).data,
            "key_id": settings.RAZORPAY_KEY_ID
        })

    def post(self, request, *args, **kwargs):
        profile_id = request.data.get("profile_id")

        if profile_id == None:
            return Response({'error': 'Profile Id Not Found'}, status=400)

        profiles = BillingProfile.objects.filter(id=profile_id)

        if not profiles.count() == 1:
            return Response({'error': 'Profile Doesn\'t exist'}, status=400)

        order = self.get_order(profiles.first())
        payment_id = request.data.get("razorpay_payment_id", None)

        if not payment_id:
            return Response({'error': 'Payment ID Not Present'}, status=400)

        razorpay_client.payment.capture(
            payment_id, order.total_in_paise())
        data = razorpay_client.payment.fetch(payment_id)
        if data.get("status") == "captured":
            done = order.mark_paid()
            if not done:
                return Response({'error': 'Unable To mark Order Paid'}, status=500)
        return Response(OrderSerializer(order).data)

    def get_order(self, profile):
        order_obj = Order.objects.get_order(profile)
        return order_obj
