# pylint: disable=no-member
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_422_UNPROCESSABLE_ENTITY, HTTP_204_NO_CONTENT
from jwt_auth.models import User
from .models import Item, Category
from .serializers import ItemSerializer, PopulatedItemSerializer, CategorySerializer
# Create your views here.

class ItemListView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, _request):
        items = Item.objects.all()
        serialized_items = PopulatedItemSerializer(items, many=True)
        return Response(serialized_items.data)

    def post(self, request):
        request.data['owner'] = request.user.id
        item = ItemSerializer(data=request.data)
        print(request.data['owner'])
        if item.is_valid():
            item.save()
            return Response(item.data, status=HTTP_201_CREATED)
        return Response(item.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)


class ItemDetailView(APIView):
    def get(self, _request, pk):
        item = Item.objects.get(pk=pk)
        serialized_item = PopulatedItemSerializer(item)
        return Response(serialized_item.data)

    def patch(self, request, pk):
        # request.data['owner'] = request.user.id
        item = Item.objects.get(pk=pk)
        updated_item = ItemSerializer(item, data=request.data)
        if updated_item.is_valid():
            updated_item.save()
            return Response(updated_item.data)
        return Response(updated_item.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        item = Item.objects.get(pk=pk)
        item.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class CategoryListView(APIView):
    def get(self, _request):
        categories = Category.objects.all()
        serialized_categories = CategorySerializer(categories, many=True)
        return Response(serialized_categories.data)

class CategoryDetailView(APIView):
    def get(self, _request, pk):
        category = Category.objects.get(pk=pk)
        serialized_category = CategorySerializer(category)
        return Response(serialized_category.data)

class BasketListView(APIView):

    def get(self, request):
        user = request.user
        print(user.id)
        basket = Item.objects.all()
        # .filter(basket=user.id)
        # print(basket)
        serializer = ItemSerializer(basket, many=True)
        # print(serializer.data)
        return Response(serializer.data)

class PurchasedListView(APIView):
    def get(self, request):
        user = request.user
        # print(user)
        purchased = Item.objects.all()
        # .filter(purchased=user.id)
        # print(purchased)
        serializer = PopulatedItemSerializer(purchased, many=True)
        # print(serializer.data)
        return Response(serializer.data)
