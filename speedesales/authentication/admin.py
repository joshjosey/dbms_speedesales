from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','phone','email','username')
    search_fields = ('id','phone','email')

# Register your models here.
admin.site.register(Customer, CustomerAdmin)