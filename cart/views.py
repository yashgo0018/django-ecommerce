import razorpay
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View

from billing.forms import AddressForm
from billing.models import BillingProfile
from order.models import Order
from products.models import Product

from .models import Cart

razorpay_client = razorpay.Client(
    auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))


class CartView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        cart_obj = Cart.objects.get_existing_or_new(request)[0]
        context = {
            "cart": cart_obj,
        }
        return render(request, "carts/home.html", context)

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
        return redirect(product_obj.get_absolute_url())


class ProfileSelectionView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        billingprofiles = request.user.billingprofile_set.all()
        context = {
            "profiles": billingprofiles,
            "title": "Billing Profiles",
            "form": AddressForm()
        }
        return render(request, "carts/profiles.html", context)


class CheckoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        profile_id = request.GET.get("profile_id")

        if profile_id == None:
            return redirect('profiles')

        cart_obj, new_obj = Cart.objects.get_existing_or_new(request)

        if cart_obj.total_cart_products() == 0:
            return redirect("cart")

        context = {
            "object": self.get_order(profile_id),
            "key_id": settings.RAZORPAY_KEY_ID
        }

        return render(request, "carts/checkout.html", context)

    def post(self, request, *args, **kwargs):
        profile_id = request.POST.get("profile_id")

        order = self.get_order(profile_id)
        payment_id = request.POST.get("razorpay_payment_id", None)

        if not payment_id:
            return redirect("cart")

        razorpay_client.payment.capture(
            payment_id, order.total_in_paise())
        data = razorpay_client.payment.fetch(payment_id)
        if data.get("status") == "captured":
            done = order.mark_paid()
            if done:
                return redirect("/")
            else:
                return redirect("cart")
        return redirect("cart")

    def get_order(self, profile_id):
        profile = BillingProfile.objects.filter(id=profile_id).first()
        order_obj = Order.objects.get_order(profile)
        return order_obj
