from .views import BillingProfileAPIView
from django.urls import path

urlpatterns = [
    path('', BillingProfileAPIView.as_view())
]
