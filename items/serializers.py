from rest_framework import serializers
# from django.contrib.auth import get_user_model
from jwt_auth.models import User, Recommendation
from .models import Item, Category

# Populating the user on to other models without including all fields
class NestedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'profile_image', 'recommendations')


class NestedItemSerializer(serializers.ModelSerializer):

    owner = NestedUserSerializer()

    class Meta:
        model = Item
        fields = ('id', 'name', 'price', 'size', 'available', 'image', 'owner', 'basket', 'purchased')


class RecommendationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recommendation
        fields = '__all__'


class NestedRecommendationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recommendation
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    items = NestedItemSerializer(many=True)
    # owner = NestedUserSerializer()

    class Meta:
        model = Category
        fields = ('id', 'name', 'category_image', 'items')


class ItemSerializer(serializers.ModelSerializer):

    owner = NestedUserSerializer

    class Meta:
        model = Item
        fields = ('id', 'owner', 'name', 'price', 'size', 'available', 'image', 'categories', 'basket', 'purchased')
        extra_kwargs = {'categories': {'required': False}}


class UserSerializer(serializers.ModelSerializer):

    recommendations = RecommendationSerializer(many=True)
    # listed_item = ListingSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'profile_image', 'recommendations')



class PopulatedUserSerializer(UserSerializer):
    recommendations = NestedRecommendationSerializer(many=True)
    # listed_item = ListingSerializer(many=True)


class PopulatedItemSerializer(ItemSerializer):
    owner = NestedUserSerializer()
    categories = CategorySerializer(many=True)
