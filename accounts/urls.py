from django.urls import path

from .views import LoginFormView, RegisterFormView, logout_page

urlpatterns = [
    path('login/', LoginFormView.as_view(), name='login'),
    path('register/', RegisterFormView.as_view(), name='register'),
    path('logout/', logout_page, name='logout'),
]
