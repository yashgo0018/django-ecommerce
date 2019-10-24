from django.urls import path

# productview  # productdetailview
from .views import ProductDetail, ProductList, FeaturedProductView
app_name = 'product'

urlpatterns = [
    path('', ProductList.as_view(), name='list'),
    path('product/q=<slug>/', ProductDetail.as_view(), name='detail'),
    path('featured/', FeaturedProductView.as_view(), name='featured'),
    path('search/', ProductList.as_view(), name='productSearch'),
]
