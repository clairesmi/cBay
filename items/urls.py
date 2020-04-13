from django.urls import path
from .views import ItemListView, ItemDetailView, CategoryListView, CategoryDetailView, BasketListView, PurchasedListView


urlpatterns = [
    path('items', ItemListView.as_view(), name='items-list'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='items-detail'),
    path('categories', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('basket', BasketListView.as_view(), name='basket-list'),
    path('purchased', PurchasedListView.as_view(), name='purchased-list')
]
