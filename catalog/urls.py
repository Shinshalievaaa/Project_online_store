from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeListView, ProductDetailView, ProductCreateView, ContactsTemplateView, ProductUpdateView

app_name = CatalogConfig.name


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('new_product/', ProductCreateView.as_view(), name='new_product'),
    path('update_product/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts')
]
