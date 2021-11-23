from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from .models import Good_Item


class ItemsListView(ListView):
    model = Good_Item
    template_name = "items_index.html"

    def get_queryset(self):
        items = Good_Item.objects.all()
        return items
