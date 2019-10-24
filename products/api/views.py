from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from products.models import Product

from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        max_price = self.request.GET.get('max_price')
        sort = self.request.GET.get('sort_by')
        keyword = self.request.GET.get('search')
        return Product.objects.filter_products(keyword, sort, max_price)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
