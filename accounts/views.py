from django.shortcuts import render
from .models import Product, Customer, Order


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders, 
        'customers': customers, 
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending, 
    }
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()
    context = {'products': products, }
    return render(request, 'accounts/products.html', context)


def customer(request, id):
    customer = Customer.objects.get(id=id)
    orders = customer.order_set.all()
    total_order = orders.count()
    context = {
        'customer': customer,
        'orders': orders,
        'total_order': total_order,
    }
    return render(request, 'accounts/customer.html', context)
