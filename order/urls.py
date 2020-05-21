from django.urls import path

from .views import CheckoutView, my_webhook_view

urlpatterns = [
    path("", CheckoutView.as_view()),
    path("hook", my_webhook_view)
]
