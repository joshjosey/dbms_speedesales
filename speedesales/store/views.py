from django.shortcuts import render
from django.contrib import messages
from .models import Product
from django.contrib.auth.models import User
from authentication.models import Customer
from cart.models import Order, Order_Product
from cart.cart import Cart
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'pages/index.html', {'products':products})

def tech(request):
    products = Product.objects.all()
    return render(request, 'pages/tech.html', {'products':products})

def food(request):
    products = Product.objects.all()
    return render(request, 'pages/tech.html', {'products':products})

def product_category(request,category):
    products = Product.objects.filter(category=category)
    cart = Cart(request)
    return render(request, 'pages/category.html', {'products':products, 'category':category})

def view_orders(request):
    user = User.objects.get(id=request.user.id)
    cust = Customer.objects.get(user=user)
    customer_orders = []
    for ord in Order.objects.filter(customer=cust):
        items = []
        subtotal = 0
        for item in Order_Product.objects.filter(order=ord):
            items.append(item)
            subtotal = subtotal + float(item.price)
        customer_orders.append((ord,items))
        total_qty = len(items)
        subtotal
        taxes = round(subtotal * 0.0825, 2)
        total_price = round(subtotal + taxes, 2)
    
    return render(request, 'pages/orders.html', {'customer_orders':customer_orders,'total_qty':total_qty, 'total_price':total_price})
