from rest_framework import serializers
from .models import Item, Category
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields= ('id, username, profile_image')

class ItemSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Item 
        fields = ('id', 'name', 'price', 'available', 'image')

class CategorySerializer(serializers.ModelSerializer):

    class Meta: 
        model = Category
        fields = ('name')