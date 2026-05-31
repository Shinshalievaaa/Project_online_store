from django.urls import path
from catalog.apps import CatalogConfig
from blog.views import BooksListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = CatalogConfig.name


urlpatterns = [
    path('blog_list/', BooksListView.as_view(), name='blog_list'),
    path('blog_detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('new_blog/', BlogCreateView.as_view(), name='new_blog'),
    path('upd_blog/<int:pk>/', BlogUpdateView.as_view(), name='upd_blog'),
    path('del_blog/<int:pk>/', BlogDeleteView.as_view(), name='del_blog'),

]
