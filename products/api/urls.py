from .views import ProductViewSet, RelatedProductView
from rest_framework import routers
from django.urls import path
router = routers.DefaultRouter()
router.register('products/list', ProductViewSet, basename="product")

urlpatterns = [
    path("related/<id>", RelatedProductView.as_view())
]
