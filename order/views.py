import json

import razorpay
import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from billing.models import BillingProfile
from cart.models import Cart
from products.models import Product

from .models import Order
from .serializers import DetailedOrderSerializer

stripe.api_key = settings.STRIPE_API_KEY

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

        cart_obj, _ = Cart.objects.get_existing_or_new(request)

        if cart_obj.total_cart_products == 0:
            return Response({'error': 'Cart Is Empty'}, status=400)

        order_obj = Order.objects.get_order(profiles.first())

        intent = stripe.PaymentIntent.create(
            customer=profiles[0].stripe_customer_id,
            amount=int(float(cart_obj.total) +
                       float(order_obj.shipping_total)) * 100,
            currency='inr',
            description=f"Order Id {order_obj.order_id}",
            # Verify your integration in this guide by including this parameter
            metadata={'integration_check': 'accept_a_payment',
                      'order_id': order_obj.order_id},
        )

        return Response({
            "order": DetailedOrderSerializer(order_obj, context={'request': request}).data,
            "secret": intent.client_secret
        })

    def post(self, request, *args, **kwargs):
        profile_id = request.data.get("profile_id")

        if profile_id == None:
            return Response({'error': 'Profile Id Not Found'}, status=400)

        profiles = BillingProfile.objects.filter(id=profile_id)

        if not profiles.count() == 1:
            return Response({'error': 'Profile Doesn\'t exist'}, status=400)

        order_obj = Order.objects.get_order(profiles.first())
        payment_id = request.data.get("razorpay_payment_id", None)

        if not payment_id:
            return Response({'error': 'Payment ID Not Present'}, status=400)

        razorpay_client.payment.capture(
            payment_id, order_obj.total_in_paise())
        data = razorpay_client.payment.fetch(payment_id)
        if data.get("status") == "captured":
            done = order_obj.mark_paid()
            if not done:
                return Response({'error': 'Unable To mark Order Paid'}, status=500)
        return Response(DetailedOrderSerializer(order_obj).data)


@csrf_exempt
def my_webhook_view(request):
    payload = request.body
    event = None
    event = stripe.Event.construct_from(
        json.loads(payload), stripe.api_key
    )
    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    # Handle the event
    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object  # contains a stripe.PaymentIntent
        desc = payment_intent.get('description', '')
        if desc.startswith("Order Id"):
            orderId = desc[9:]
            order_obj: Order = Order.objects.filter(order_id=orderId).first()
            order_obj.mark_paid()
    else:
        return HttpResponse(status=400)

    return HttpResponse(status=200)
