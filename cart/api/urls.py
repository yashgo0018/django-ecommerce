from .views import CartAPIView, CheckProductInCart
from rest_framework import routers
from django.urls import path

router = routers.DefaultRouter()

urlpatterns = [
    path('', CartAPIView.as_view()),
    path('<product_id>/', CheckProductInCart.as_view()),
]
