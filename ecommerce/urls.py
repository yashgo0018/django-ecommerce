from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from errors.views import bad_request
from billing.views import BillingProfileAddForm
from django.conf.urls import url, include
from django.contrib.auth.models import User

handler404 = bad_request

admin.site.site_title = 'eCommerce'
admin.site.index_title = 'Admin'
admin.site.site_header = 'eCommerce Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('billing_profile/add/', BillingProfileAddForm.as_view()),
    path('accounts/', include('accounts.urls')),
    path('', include('products.urls', namespace='products')),
    path('cart/', include('cart.urls')),
    path('user/', include(('users.urls', 'users'), namespace='users')),
    path('api/', include('ecommerce.api_urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
