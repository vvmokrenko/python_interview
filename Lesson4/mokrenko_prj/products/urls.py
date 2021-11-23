from django.conf.urls import url
from .views import ItemsListView

urlpatterns = [
    url(r'', ItemsListView.as_view()),
]