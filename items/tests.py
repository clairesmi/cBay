# # pylint: disable=no-member
# from django.urls import reverse
# from rest_framework.test import APITestCase
# from .models import Item, Category

# # Create your tests here.
# class ItemsTests(APITestCase):

#     def setUp(self):
#         item = Item.objects.create(name='Red Dress', price=40.0, available=True, size="S")
#         category = Category.objects.create(name='dresses')
#         item.categories.set([category])

#     def test_items_index(self):
#         """
#         Should return an array of items
#         """
#         url = reverse('items-list')
#         response = self.client.get(url)

#         self.assertEqual(response.status_code, 200)
#         self.assertJSONEqual(response.content, [{
#             'id': 1,
#             'name': 'Red Dress',
#             'price': 40.0,
#             'available': True,
#             "size": "S",
#             'image': 'https://d2h1pu99sxkfvn.cloudfront.net/b0/9669358/390927964_VHR71smkgh/P0.jpg',
#             "owner": 2,
#             "categories": [{
#             'id': 1,
#             'name': 'dresses'
#             }]
#         }])
