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

    def get_order(self, billing_profile):
        orders = super().get_queryset().filter(
            billing_profile=billing_profile, status='created')
        if len(orders) == 0:
            order = Order(billing_profile=billing_profile,
                          cart=billing_profile.user.cart_set.filter(used=False).first())
            order.save()
            return order
        return orders.first()


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
        default=1.99, max_digits=10, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    objects = OrderManager()

    def __str__(self):
        return self.order_id

    def update_total(self):
        cart_total = self.cart.total
        if cart_total == 0:
            self.shipping_total = 0
        else:
            self.shipping_total = 1.99
        self.save()
        ship_total = self.shipping_total
        new_total = float(cart_total) + float(ship_total)
        self.total = new_total
        self.save()
        return new_total

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


def pre_save_create_order_id(sender, instance, *args, **kwargs):
    print(instance.cart.total, instance.shipping_total)
    if not instance.order_id:
        instance.order_id = unique_product_id_generator(instance)


pre_save.connect(pre_save_create_order_id, sender=Order)


def post_save_order_total(sender, instance, created, *args, **kwargs):
    if not created:
        cart_obj = instance
        #cart_total = cart_obj.total
        cart_id = cart_obj.id
        qs = Order.objects.filter(cart__id=cart_id)
        if qs.count() == 1:
            order_obj = qs.first()
            order_obj.update_total()


post_save.connect(post_save_order_total, sender=Cart)


def post_save_order(sender, instance, created, *args, **kwargs):
    if created:
        instance.update_total()


post_save.connect(post_save_order, sender=Order)
