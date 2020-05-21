from .views import BillingProfileAPIView, CountriesData
from django.urls import path

urlpatterns = [
    path('', BillingProfileAPIView.as_view()),
    path('countries/', CountriesData.as_view())
]
