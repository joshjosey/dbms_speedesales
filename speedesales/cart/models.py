from django.db import models
import uuid
import datetime
from authentication.models import Customer
from store.models import Product
# Create your models here.

class Order(models.Model): #order data
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2, default=0.00)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return  f"{self.id}"
    
class Order_Product(models.Model): #links the order with the products
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10,decimal_places=2, default=0.00)

    def __str__(self):
        return f"Order {self.order} contains {self.quantity} of {self.product}"