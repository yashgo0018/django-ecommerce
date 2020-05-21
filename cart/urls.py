from django.urls import path
from rest_framework import routers

from .views import CartAPIView, CheckProductInCart

router = routers.DefaultRouter()

urlpatterns = [
    path('', CartAPIView.as_view()),
    path('<product_id>/', CheckProductInCart.as_view()),
]
