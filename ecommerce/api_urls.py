from django.urls import path, include
from .routers import DefaultRouter
from products.api.urls import router as product_router
from accounts.api.urls import router as account_router
from cart.api.urls import router as cart_router
router = DefaultRouter()
router.extend(account_router)
router.extend(product_router)
router.extend(cart_router)

urlpatterns = [
    path('', include(router.urls)),
    path('accounts/', include('accounts.api.urls')),
    path('products/', include('products.api.urls')),
    path('cart/', include('cart.api.urls')),
    path('checkout/', include('order.api.urls')),
    path('profiles/', include('billing.api.urls')),
]
