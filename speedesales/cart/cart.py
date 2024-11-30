from store.models import Product
from .models import Order
from .models import Order_Product

class Cart():
    def __init__(self, request):
        self.session = request.session
        self.request = request

        #check if a session exists
        cart = self.session.get('session_key')
        
        #create a session if not
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #make the cart global to the site
        self.cart = cart
    
    def add(self, product, quantity):
        #convert UUID into a string
        product_id = str(product.id)

        #check if the product is in the cart and increment or add if not
        if product_id in self.cart:
            #get the old data
            old_qty = int(self.cart[product_id]['qty'])
            old_price =  float(self.cart[product_id]['unit_price'])

            #calculate the new data
            new_qty = old_qty + quantity
            new_price = round(old_price * new_qty, 2 )

            #assign the new data to the cart
            self.cart[product_id]['qty'] = str( new_qty )
            self.cart[product_id]['total_price'] = str( new_price )
        else:
            self.cart[product_id] = {'qty':str(quantity),'unit_price': str(product.price),'total_price': str(product.price*quantity)}
        #tell the APi that the session has been edited
        self.session.modified = True


    '''
    Method to calculte the total quantity of items in the cart
    '''
    def get_qty(self):
        qty = 0
        for item in self.cart:
            qty = qty + int(self.cart[item]['qty'])
            #print(qty)
        return qty

    '''
    Method to get the quantity of a specific item
    '''
    def get_item_qty(self, product):
        if product in self.cart:
            qty = self.cart[product]['qty']
        else:
            qty = -1
        return qty

    '''
    Method to calculte the total price of items in the cart
    ''' 
    def get_price(self):
        price = 0.00
        for item in self.cart:
            price = price + float(self.cart[item]['total_price'])
            #print(price)
        return round(price,2)
    
    '''
    Method to get all items in the cart
    '''
    def get_items(self):
        #grab each item id from the cart
        item_ids = self.cart.keys()

        #get item data
        items_in_cart = Product.objects.filter(id__in=item_ids)
        
        #return the items in the cart
        #print(items_in_cart)
        return items_in_cart
    
    def update(self,product,quantity):
         #convert UUID into a string
        product_id = str(product)
        print(quantity)
        #check if the product is in the cart and increment or add if not
        if product_id in self.cart:
            #get the old data
            old_qty = int(self.cart[product_id]['qty'])
            old_price =  float(self.cart[product_id]['unit_price'])

            #calculate the new data
            new_qty = quantity
            new_price = round(old_price * new_qty, 2 )

            #assign the new data to the cart
            self.cart[product_id]['qty'] = str( new_qty )
            self.cart[product_id]['total_price'] = str( new_price )
        else:
            return
        
        self.session.modified = True

    def remove(self, product):
        #convert UUID into a string
        product_id = str(product)

        #remove the item if it is in the cart
        removedItem = self.cart.pop(product_id, None)
        
        
        self.get_items()
        #self.get_qty()
        #self.get_price()
        self.session.modified = True
        return removedItem
    
    def confirm(self):
        pass