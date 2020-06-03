from django.urls import path
from .views import home, products, customer, create_order, update_order, delete_order

urlpatterns = [
    path('', home, name='home'),
    path('products', products, name='products'),
    path('customer/<int:id>', customer, name='customer'),
    path('create/order/<int:id>', create_order, name='create-order'),
    path('update/order/<int:id>', update_order, name='update-order'),
    path('delete/order/<int:id>', delete_order, name='delete-order'),
]

