from django.urls import path
from rest_framework import routers

from .views import ProductViewSet, RelatedProductView

router = routers.DefaultRouter()
router.register('products/list', ProductViewSet, basename="product")

urlpatterns = [
    path("related/<id>", RelatedProductView.as_view())
]
