from django.core.cache import cache

from config.settings import CACHE_ENABLED
from .models import Product

class ProductService:

    @staticmethod
    def list_products_in_category(category_id):
        if not CACHE_ENABLED:
            return None
        key_name = f'my_queryset_{category_id}'
        products = cache.get(key_name)

        if products is not None:
            return products

        products = Product.objects.filter(category_id=category_id)
        cache.set(key_name, products, 60 * 15)
        return products
