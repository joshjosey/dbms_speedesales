from django.contrib import admin
from .models import Order,Order_Product

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','customer','date','status')
    list_filters = ('customer','status')
    search_fields = ('id','customer','date')

class Order_Product_Admin(admin.ModelAdmin):
    list_display = ('order','product','quantity','price')
    list_filters = ('order','product')
    search_fields = ('order','product')


admin.site.register(Order, OrderAdmin)
admin.site.register(Order_Product, Order_Product_Admin)
