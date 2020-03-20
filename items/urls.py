from django.urls import path
from .views import ItemListView, ItemDetailView, CategoryListView, CategoryDetailView, BasketListView, PurchasedListView


urlpatterns = [
    path('items', ItemListView.as_view()),
    path('items/<int:pk>/', ItemDetailView.as_view()),
    path('categories', CategoryListView.as_view()),
    path('categories/<int:pk>/', CategoryDetailView.as_view()),
    path('basket', BasketListView.as_view()),
    path('purchased', PurchasedListView.as_view())
]
