from django.contrib import admin
from .models import Category, Product
from django.utils.html import format_html

#define the admin views
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','category','description','image', 'featured')
    list_filters = ('category', 'featured')
    search_fields = ('id','name','category')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
