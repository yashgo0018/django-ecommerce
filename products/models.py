from os import path
from random import randint

from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save
from django.urls import reverse

from ecommerce.settings import MEDIA_URL
from ecommerce.utils import unique_slug_generator


def get_filename_ext(filename):
    filepath = path.basename(filename)
    name, ext = path.splitext(filepath)
    return name, ext


def upload_name_path(instance, filename):
    folderName = randint(1, 40000000)
    filenam = randint(1, folderName)
    ext = get_filename_ext(filename)[1]
    return f'products/{folderName}/{filenam}.{ext}'


class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def filter_products(self, keyword, sort, min_price, max_price):
        qs = self.get_queryset().filter(active=True)
        if keyword:
            qs = qs.filter(
                Q(tag_list__title__icontains=keyword) |
                Q(title__icontains=keyword)
            ).distinct()
        if sort:
            sort = int(sort)
            if sort == 2:
                qs = qs.order_by('-price')
            elif sort == 1:
                qs = qs.order_by('price')
        if max_price:
            max_price = int(max_price)
            qs = qs.filter(price__lt=max_price)
        if min_price:
            min_price = int(min_price)
            qs = qs.filter(price__gt=min_price)
        return qs

    def get_products(self):
        return self.get_queryset().filter(active=True)


class Product(models.Model):
    image = models.ImageField(upload_to=upload_name_path, null=True)
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    description = RichTextField()
    original_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=4, decimal_places=2, default=18)

    objects = ProductManager()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.slug})

    def get_related_products(self):
        title_split = self.title.split(' ')
        lookups = Q(title__icontains=title_split[0])

        for i in title_split[1:]:
            lookups |= Q(title__icontains=i)

        for i in self.tag_list.all():
            lookups |= Q(tag_list__title__icontains=i.title)

        related_products = Product.objects.filter(
            lookups).distinct().exclude(id=self.id)
        return related_products

    def get_image_url(self):
        return f'{MEDIA_URL}{self.image}'


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)


class Tag(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    product = models.ManyToManyField(
        Product, blank=True, related_name="tag_list")

    def __str__(self):
        return self.title


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_receiver, sender=Tag)
