from django.contrib import admin
from .models import Customer, Employee

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','user','phone','address','city','state','zip','country','current_cart'
)
    search_fields = ('id','phone')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','user','phone','department')
    search_fields = ('id','phone','department')
    list_filter = ('department',)

# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Employee, EmployeeAdmin)