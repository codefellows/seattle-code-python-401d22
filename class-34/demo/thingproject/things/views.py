from django.views.generic import ListView, DetailView
from .models import Thing


class ThingListView(ListView):
    template_name = "home.html"
    model = Thing
    context_object_name = 'things'


class ThingDetailView(DetailView):
    template_name = 'thing_detail.html'
    model = Thing
