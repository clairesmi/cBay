# pylint: disable=no-member
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Item, Category

# Create your tests here.
class ItemsTests(APITestCase):

    def setUp(self):
        item = Item.objects.create(name='purple dress', price=10.99, available=True, size=10)
        category = Category.objects.create(name='dresses')
        item.categories.set([category])
