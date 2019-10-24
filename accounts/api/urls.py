from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import RegisterView, GetUserView

router = routers.DefaultRouter()

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('register/', RegisterView.as_view()),
    path('get_user/', GetUserView.as_view())
]
