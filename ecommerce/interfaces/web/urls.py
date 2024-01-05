# ecommerce/interfaces/web/urls.py
from django.urls import path
from .views import create_order, create_user, create_product

urlpatterns = [
    path('create_order/', create_order, name='create_order'),
    path('create_user/', create_user, name='create_user'),
    path('create_product/', create_product, name='create_product'),
    # Add other URL patterns as needed
]
