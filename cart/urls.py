from django.urls import path

from .views import CartAPIView, CheckProductInCart

urlpatterns = [
    path('', CartAPIView.as_view()),
    path('<product_id>/', CheckProductInCart.as_view()),
]
