from django.shortcuts import render
from .models import Product

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
    return render(request, 'pages/category.html', {'products':products, 'category':category})