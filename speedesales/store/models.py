from django.db import models
import uuid
import datetime
from authentication.models import Customer
# Create your models here.
class Category(models.Model): #product categories
    name = models.CharField(primary_key=True,max_length=50)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'

class Product(models.Model): #product data
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2, default=0.00)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='General')
    description = models.TextField(default="",blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/', default='placeholder.jpg')
    
    #featured items
    featured = models.BooleanField(default="False")

    def __str__(self):
        return self.name