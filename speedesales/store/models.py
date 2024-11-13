from django.db import models
import uuid
import datetime

# Create your models here.
class Category(models.Model): #product categories
    name = models.CharField(primary_key=True,max_length=50)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'
class Customer(models.Model): #customer data
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Customer {self.id}: {self.first_name} {self.last_name}"

class Product(models.Model): #product data
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2, default=0.00)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='feneral')
    description = models.TextField(default="",blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/', default='placeholder.jpg')
    
    #featured items
    featured = models.BooleanField(default="False")

    def __str__(self):
        return self.name

class Order(models.Model): #order data
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.id
    
class Order_Product(models.Model): #links the order with the products
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"Order {self.order} contains {self.quantity} of {self.product}"