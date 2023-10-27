from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import order,order_item
# Register your models here.

class orderInLine(admin.TabularInline):
    model=order_item
    fields=['order','product','quantity','price']
    extra=0


@admin.register(order)
class orderAdmin(ModelAdmin):
    list_display=['user','first_name','last_name','phone_number','address','email','is_payed']
    inlines=[
        orderInLine,
    ]
    
# @admin.register(order_item) 
# class order_itemAdmin(ModelAdmin):
#     list_display=['order','product','quantity','price']