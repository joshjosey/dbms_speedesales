from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .cart import Cart
from .models import Order, Order_Product
from django.contrib.auth.models import User
from authentication.models import Customer
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
    #create a cart variable
    cart = Cart(request)
    for item in cart.get_items:
        cart.remove(product=item.id)

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

def checkout(request):
    # Get cart
    cart = Cart(request)
    
    # Get the items in the cart
    items_in_cart = cart.get_items()
    subtotal = cart.get_price()
    taxes = round(subtotal * 0.0825, 2)
    total = round(subtotal + taxes, 2)
    qty = cart.get_qty()

    #get the customer data
    customer = Customer.objects.get(id=request.user.id)

    #get the quantity and total price for each item
    cart_data = []
    for product in items_in_cart:
        product_qty = cart.get_item_qty(str(product.id))
        product_price = round(float(product.price)*float(product_qty),2)
        cart_data.append((product,product_qty,product_price))  

    if  request.POST.get('action') == 'post':
        #create the order
        order = Order(customer=customer, price=total)
        order.save()

        #attach items to the order
        for product,quantity,price in cart_data:
            order_prod = Order_Product(order=order,product=product,quantity=quantity,price=price)
            print(order_prod)
            order_prod.save()
        
        return redirect('index')
    else:
        # Render the page and send the items and their quantities
        return render(request, "checkout.html", {"cart_data": cart_data,"subtotal": subtotal,"taxes": taxes,"total": total,"qty": qty,})

def confirm_checkout(request):
    cart = Cart(request)
    print(request)
    if request.user.is_authenticated:
        
        return redirect('checkout')
    else:

        return redirect('authentication:login',{"cart"})
    pass