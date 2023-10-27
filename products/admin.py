from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import category, product , comment 
# Register your models here.



class orderInLine(admin.TabularInline):
    model=product
    fields=['title','price','inventory']
    extra=0
@admin.register(category)
class categoryAdmin(ModelAdmin):
    list_display=['title','descriptions']
    inlines=[
        orderInLine,
    ]
@admin.register(product)
class productAdmin(ModelAdmin):
    list_display=['title','des','price','datetime_add','image']
    
@admin.register(comment) 
class CommentAdmin(ModelAdmin):
    list_display=['text','rate','user','product','datetime_add','active']