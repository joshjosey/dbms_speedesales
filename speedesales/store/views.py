from django.shortcuts import render
from django.contrib import messages
from .models import Product
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