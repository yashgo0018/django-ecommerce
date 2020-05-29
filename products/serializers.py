from rest_framework import serializers
from rest_framework.fields import Field, ListField, SerializerMethodField

from .models import Product, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title', 'slug', 'product']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    tag_list = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'image', 'title', 'slug',
                  'featured', 'description', 'original_price', 'price', "tag_list"]
