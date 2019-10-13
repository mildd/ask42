from django.urls import path

from testapp.views import index_view, NameListView

urlpatterns = [
    path('', index_view),
    path('names/', NameListView.as_view())
]