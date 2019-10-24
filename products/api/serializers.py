from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'url', 'image', 'title', 'slug', 'active',
                  'featured', 'description', 'original_price', 'price']
