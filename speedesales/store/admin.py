from django.contrib import admin
from .models import Category, Product, Order, Order_Product
from django.utils.html import format_html

#define the admin views
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','category','description','image', 'featured')
    list_filters = ('category', 'featured')
    search_fields = ('id','name','category')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','customer','address','date','status')
    list_filters = ('customer','status')
    search_fields = ('id','customer','date')

class Order_Product_Admin(admin.ModelAdmin):
    list_display = ('order','product','quantity')
    list_filters = ('order','product')
    search_fields = ('order','product')


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Order_Product, Order_Product_Admin)
