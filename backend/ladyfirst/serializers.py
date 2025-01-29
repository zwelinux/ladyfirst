from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product 


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['user', 'title', 'brand_name', 'size', 'condition', 'original_price', 'second_hand_price', 'description', 'image_urls', 'authenticity_docs', 'status', 'created_at']