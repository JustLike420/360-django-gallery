from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .forms import CardCreateForm
from .models import Card


# Create your views here.
class Home(ListView):
    model = Card
    template_name = 'home.html'
    context_object_name = 'cards'


class PhotoDetail(DetailView):
    model = Card
    template_name = 'detail.html'
    context_object_name = 'card'


class CreateCard(CreateView):
    form_class = CardCreateForm
    template_name = 'new_post.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('home')
