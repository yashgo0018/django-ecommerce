from django.db import models
from django.db.models.signals import post_save, pre_save

from billing.models import BillingProfile
from cart.models import Cart
from ecommerce.utils import unique_product_id_generator

STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
    ('refunded', 'Refunded'),
)


class OrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter()

    def get_order(self, billing_profile: BillingProfile):
        qs = self.get_queryset().filter(
            billing_profile__user=billing_profile.user, status='created')
        if qs.count() == 0:
            cart = billing_profile.user.cart_set.filter(used=False).first()
            order = Order(billing_profile=billing_profile, cart=cart)
            order.save()
            return order
        else:
            order = qs.first()
            order.billing_profile = billing_profile
            order.save()
            return order


class Order(models.Model):
    billing_profile = models.ForeignKey(
        BillingProfile, on_delete=models.CASCADE, null=True, blank=True)
    order_id = models.CharField(max_length=120, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    status = models.CharField(choices=STATUS_CHOICES,
                              default='created', max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    shipping_total = models.DecimalField(
        default=70, max_digits=10, decimal_places=2)

    objects = OrderManager()

    def __str__(self):
        return self.order_id

    @property
    def total_in_paise(self):
        return int(self.total * 100)

    def check_done(self):
        billing_profile = self.billing_profile
        total = self.total
        cart = self.cart
        active = self.active
        if active and total > 0 and cart and billing_profile:
            return True
        return False

    def mark_paid(self):
        if self.check_done():
            self.cart.used = True
            self.cart.save()
            self.status = 'paid'
            self.save()
            return True
        return False

    @property
    def cart_total(self):
        return self.cart.total

    @property
    def tax_total(self):
        return self.cart.tax_total

    @property
    def total(self):
        return float(self.cart_total) + float(self.tax_total) + float(self.shipping_total)


def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_product_id_generator(instance)


pre_save.connect(pre_save_create_order_id, sender=Order)
