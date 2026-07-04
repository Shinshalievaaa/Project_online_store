from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse

from catalog.forms import ProductForm, ModeratorProductForm
from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:home')

    def get_form_class(self):
        user = self.request.user
        if user.has_perm('catalog.can_unpublish_product'):
            return ModeratorProductForm
        else:
            return ProductForm


class ContactsTemplateView(TemplateView):
    template_name = 'contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        print(name, phone, message)
        return HttpResponse('Данные успешно отправлены')


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'catalog.delete_product'
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('catalog:home')
