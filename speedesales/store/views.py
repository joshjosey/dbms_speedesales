from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'pages/index.html', {'products':products})

def tech(request):
    products = Product.objects.all()
    return render(request, 'pages/tech.html', {'products':products})