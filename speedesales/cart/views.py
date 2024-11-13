from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.
def view_cart(request):
    #load the cart in
    cart = Cart(request)
    
    #get the items in the cart
    items_in_cart = cart.get_items()
    subtotal = cart.get_price()
    taxes = round(subtotal*0.0825,2)
    total = round(subtotal+taxes,2)
    qty = cart.get_qty()
    #render the page and send it the items in the cart
    return render(request, "view_cart.html", {"items_in_cart":items_in_cart,"subtotal":subtotal,"taxes":taxes,"total":total,"qty":qty})

def add_to_cart(request):
    #create a cart variable
    cart = Cart(request)

    #POST is from a webpage, post is from JS
    if request.POST.get('action') == 'post':
        #extract the id
        product_id = (request.POST.get('id'))

        #get the item from the db
        product = Product.objects.get(id=product_id)

        #ensure that quantity is an integer
        product_qty = int(request.POST.get('qty'))

        #save to the cookie session
        cart.add(product=product,quantity=product_qty)

        #get the total amt of items in the cart
        cart_qty = cart.get_qty()
        cart_price = cart.get_price()

        response = JsonResponse({'qty':cart_qty})
        return response

def remove_from_cart(request):
    pass

def update_cart(request):
    pass