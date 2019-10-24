from django.urls import path

from .views import CheckoutView, ProfileSelectionView, CartView

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('profiles/', ProfileSelectionView.as_view(), name='profiles'),
]
