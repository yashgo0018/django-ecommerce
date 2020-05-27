from django.shortcuts import get_object_or_404
from rest_framework import authentication, permissions
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        max_price = self.request.GET.get('max_price')
        min_price = self.request.GET.get('min_price')
        sort = self.request.GET.get('sort')
        keyword = self.request.GET.get('keyword')
        return Product.objects.filter_products(keyword, sort, min_price, max_price)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class RelatedProductView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, id, *args, **kwargs):
        product_id = id  # request.data.get("product_id")
        print(id)
        if not product_id:
            return Response({"error": "Product Id Not Found"}, status=400)
        product = get_object_or_404(Product, id=product_id)
        products_serialized = ProductSerializer(
            product.get_related_products(), many=True, context={'request': request})
        return Response(products_serialized.data)

    @classmethod
    def get_extra_actions(cls):
        return []
