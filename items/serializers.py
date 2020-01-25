from rest_framework import serializers
from .models import Item, Category
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields  = ('id', 'username', 'email', 'profile_image')

class NestedItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'name', 'price', 'available', 'image')        


class CategorySerializer(serializers.ModelSerializer):

    items = NestedItemSerializer(many=True)

    class Meta: 
        model = Category
        fields = ('id', 'name', 'items')


class ItemSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Item 
        fields = ('id', 'owner', 'name', 'price', 'available', 'image', 'categories')
        extra_kwargs = {'comments': {'required': False}, 'categories': {'required': False}}   


class PopulatedItemSerializer(ItemSerializer):
    owner = UserSerializer()
    categories = CategorySerializer(many=True)


class PopulatedCategorySerializer(CategorySerializer):
    items = NestedItemSerializer(many=True)