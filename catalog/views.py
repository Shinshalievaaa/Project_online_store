from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from catalog.forms import ProductForm, ModeratorProductForm
from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from catalog.services import ProductService


class HomeListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'home.html'


@method_decorator(cache_page(60*15), name = 'dispatch')
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

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:home')

    def get_form_class(self):
        user = self.request.user
        if user.has_perm('catalog.can_unpublish_product'):
            return ModeratorProductForm
        if user == self.object.owner:
            return ProductForm
        raise PermissionDenied


class ContactsTemplateView(TemplateView):
    template_name = 'contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        print(name, phone, message)
        return HttpResponse('Данные успешно отправлены')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    # permission_required = 'catalog.delete_product'
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('catalog:home')


class ProductInCategoryListView(ListView):
    model = Product
    template_name = 'list_products_in_category.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        queryset = ProductService.list_products_in_category(category_id)
        return queryset
