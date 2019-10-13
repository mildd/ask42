from django.shortcuts import render
from django.utils import six
from django.views.generic import ListView

from .models import NameModel


def index_view(request):
    if request.method == 'POST':
        query = dict(six.iterlists(request.POST))
        query.pop('csrfmiddlewaretoken')
        names = NameModel(names=query)
        names.save()
    return render(request, 'index.html')


class NameListView(ListView):
    template_name = 'names.html'
    queryset = NameModel.objects.all()
