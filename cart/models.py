from django.contrib.auth import get_user_model
from django.db import models

from products.models import Product

User = get_user_model()


class CartManager(models.Manager):
    def get_existing_or_new(self, request):
        created = False
        cart_id = request.session.get('cart_id')
        if self.get_queryset().filter(id=cart_id, used=False).count() == 1:
            obj = self.model.objects.get(id=cart_id)
        elif self.get_queryset().filter(user=request.user, used=False).count() == 1:
            obj = self.model.objects.get(user=request.user, used=False)
            request.session['cart_id'] = obj.id
        else:
            obj = self.model.objects.create(user=request.user)
            request.session['cart_id'] = obj.id
            created = True
        return obj, created


class Cart(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    used = models.BooleanField(default=False)

    objects = CartManager()

    def __str__(self):
        return str(self.id)

    @property
    def total(self):
        total = 0
        for product in self.products.all():
            total += float(product.price)
        return str(total)[:(str(total).find('.')+3)]

    def total_cart_products(self):
        return self.products.count()
