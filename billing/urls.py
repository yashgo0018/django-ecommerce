from django.urls import path

from .views import BillingProfileAPIView, CountriesData

urlpatterns = [
    path('', BillingProfileAPIView.as_view()),
    path('countries/', CountriesData.as_view())
]
