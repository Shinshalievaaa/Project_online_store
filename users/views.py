# from users.forms import ProductForm
from users.models import CustomUser
from django.views.generic.edit import CreateView
# from django.urls import reverse_lazy


class HomeListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'home.html'
from django.shortcuts import render

# Create your views here.
