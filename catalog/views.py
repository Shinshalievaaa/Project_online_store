from django.http import HttpResponse
from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class HomeListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'home.html'


class ProductDetailView(DetailView):
    model = Product
    fields = ['name', 'description', 'image_product', 'category', 'price']
    context_object_name = 'product'
    template_name = 'product_detail.html'


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'image_product', 'category', 'price']
    context_object_name = 'product'
    template_name = 'new_product.html'
    success_url = reverse_lazy('catalog:home')


class ContactsTemplateView(TemplateView):
    template_name = 'contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        print(name, phone, message)
        return HttpResponse('Данные успешно отправлены')
