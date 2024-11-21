from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.
def view_cart(request):
    # Load the cart
    cart = Cart(request)
    
    # Get the items in the cart
    items_in_cart = cart.get_items()
    subtotal = cart.get_price()
    taxes = round(subtotal * 0.0825, 2)
    total = round(subtotal + taxes, 2)
    qty = cart.get_qty()
    cart_data = [(product, cart.get_item_qty(str(product.id))) for product in items_in_cart]
    
    # Render the page and send the items and their quantities
    return render(request, "view_cart.html", {
        "cart_data": cart_data,
        "subtotal": subtotal,
        "taxes": taxes,
        "total": total,
        "qty": qty
    })


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
        subtotal = cart.get_price()
        taxes = round(subtotal*0.0825,2)
        total = round(subtotal+taxes,2)

        response = JsonResponse({
            'qty':cart_qty,
            'subtotal':subtotal,
            'taxes':taxes,
            'total':total})

        return response

def empty_cart(request):
    pass

def remove_from_cart(request):
    #create a cart variable
    cart = Cart(request)

    #POST is from a webpage, post is from JS
    if request.POST.get('action') == 'post':
        #extract the id
        product_id = (request.POST.get('id'))

        #save to the cookie session
        cart.remove(product=product_id)

        #get the total amt of items in the cart
        cart_qty = cart.get_qty()
        subtotal = cart.get_price()
        taxes = round(subtotal*0.0825,2)
        total = round(subtotal+taxes,2)

        response = JsonResponse({
            'qty':cart_qty,
            'subtotal':subtotal,
            'taxes':taxes,
            'total':total})
        return response

def update_cart(request):
    cart = Cart(request)
    
    #POST is from a webpage, post is from JS
    if request.POST.get('action') == 'post':
        #extract the id as a stirng
        product = str(request.POST.get('id'))

        #ensure that quantity is an integer
        product_qty = int(request.POST.get('qty'))

        cart.update(product=product,quantity=product_qty)

        cart_qty = cart.get_qty()
        subtotal = cart.get_price()
        taxes = round(subtotal*0.0825,2)
        total = round(subtotal+taxes,2)
        item_qty = cart.get_item_qty(product)
        print(item_qty)

        response = JsonResponse({
            'item_qty':item_qty,
            'qty':cart_qty,
            'subtotal':subtotal,
            'taxes':taxes,
            'total':total})
        return response