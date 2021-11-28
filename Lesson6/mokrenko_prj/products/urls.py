from django.urls import path
from .views import ItemsListView, CategoryListView, goods_by_category

app_name = 'products'

urlpatterns = [
    path('', ItemsListView.as_view()),
    path('', CategoryListView.as_view(), name='category'),
    path('<slug:category_slug>', goods_by_category, name='products_by_category'),
]