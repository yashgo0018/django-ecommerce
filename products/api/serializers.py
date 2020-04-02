from rest_framework import serializers
from products.models import Product, Tag
from rest_framework.fields import Field, SerializerMethodField, ListField


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title', 'slug', 'product']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    tag_list = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'url', 'image', 'title', 'slug',
                  'featured', 'description', 'original_price', 'price', "tag_list"]  # , "get_related_products"]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
