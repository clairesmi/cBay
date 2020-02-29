from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Item, Category
User = get_user_model()

class NestedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'profile_image')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'profile_image')


class NestedItemSerializer(serializers.ModelSerializer):

    owner = NestedUserSerializer()

    class Meta:
        model = Item
        fields = ('id', 'name', 'price', 'size', 'available', 'image', 'owner')


class CategorySerializer(serializers.ModelSerializer):

    items = NestedItemSerializer(many=True)
    # owner = NestedUserSerializer()

    class Meta:
        model = Category
        fields = ('id', 'name', 'items')


class ItemSerializer(serializers.ModelSerializer):

    owner = NestedUserSerializer()

    class Meta:
        model = Item
        fields = ('id', 'owner', 'name', 'price', 'size', 'available', 'image', 'categories')
        extra_kwargs = {'categories': {'required': False}}


class PopulatedItemSerializer(ItemSerializer):
    owner = NestedUserSerializer()
    categories = CategorySerializer(many=True)


# class PopulatedCategorySerializer(CategorySerializer):
#     owner = NestedUserSerializer()
#     items = NestedItemSerializer(many=True)
