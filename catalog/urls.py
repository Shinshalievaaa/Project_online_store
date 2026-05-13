from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, product_detail, contacts

app_name = CatalogConfig.name


urlpatterns = [
    path('', home, name='home'),
    path('product_detail/<int:product_id>/', product_detail, name='product_detail'),
    path('contacts/', contacts, name='contacts'),
]
