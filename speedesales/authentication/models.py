from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import uuid

# Create your models here.
class Customer(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=200,blank=True)
    city = models.CharField(max_length=200,blank=True)
    state = models.CharField(max_length=200,blank=True)
    zip = models.CharField(max_length=200,blank=True)
    country = models.CharField(max_length=200,blank=True)
    current_cart = models.CharField(max_length=500,blank=True)

    def __str__(self):
        return f"Customer {self.user.username}: {self.user.first_name} {self.user.last_name}"
    
#add customers on signup
def create_customer(sender, instance, created, **kwargs):
        if created:
            user_profile = Customer(user=instance)
            user_profile.save()

post_save.connect(create_customer,sender=User)
    
class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user =  models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee',unique=True)
    phone = models.CharField(max_length=10)
    department = models.ForeignKey('store.Category', on_delete=models.CASCADE, default='General')


    def __str__(self):
        return f"Customer {self.id}: {self.first_name} {self.last_name}"
