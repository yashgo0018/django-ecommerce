from django.urls import path
from .views import user_order, user_address, user_security

urlpatterns = [
    path('orders/', user_order, name='orders'),
    path('security', user_security, name='security'),
    path('address/', user_address, name='address'),
]