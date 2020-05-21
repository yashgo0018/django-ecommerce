from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from accounts.urls import router as account_router
from cart.urls import router as cart_router
from products.urls import router as product_router

from .routers import DefaultRouter

admin.site.site_title = 'eCommerce'
admin.site.index_title = 'Admin'
admin.site.site_header = 'eCommerce Administration'

router = DefaultRouter()
router.extend(account_router)
router.extend(product_router)
router.extend(cart_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('order.urls')),
    path('profiles/', include('billing.urls')),
]

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
