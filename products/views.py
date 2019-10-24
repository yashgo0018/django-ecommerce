from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView

from cart.models import Cart

from .forms import FilterForm  # PriceRangeForm, SortForm, SearchForm
from .models import Product
from django.urls import resolve


class ProductList(ListView):
    model = Product
    context_object_name = 'model'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter_form = FilterForm(self.request.GET or None)
        context['pricerange'] = filter_form
        return context

    def get_queryset(self):
        url_name = resolve(self.request.path).url_name
        max_price = self.request.GET.get('max_price')
        sort = self.request.GET.get('sort_by')
        keyword = self.request.GET.get('search')
        qs = self.model.objects.filter_products(keyword, sort, max_price)
        return qs


class FeaturedProductView(ProductList):
    def get_queryset(self):
        return super().get_queryset().filter(featured=True)


class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            cart_obj, new_obj = Cart.objects.get_existing_or_new(self.request)
            context['cart'] = cart_obj
        return context
