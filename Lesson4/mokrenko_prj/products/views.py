from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from .models import Good_Item, Category


class ItemsListView(ListView):
    model = Good_Item
    template_name = "goods_list.html"

    def get_queryset(self):
        items = Good_Item.objects.prefetch_related('category').all()
        return items


class CategoryListView(ListView):
    model = Category
    template_name = "category_list.html"

    def get_queryset(self):
        items = Category.objects.all()
        return items


def goods_by_category(request, category_slug):
    items = Category.objects.all().filter(slug=category_slug)
    print('items=', items)

    return render(request, 'goods_category.html', {'categories': items})