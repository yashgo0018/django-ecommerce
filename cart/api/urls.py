from .views import CartAPIView
from rest_framework import routers
from django.urls import path
router = routers.DefaultRouter()
urlpatterns = [
    path('', CartAPIView.as_view()),
]
