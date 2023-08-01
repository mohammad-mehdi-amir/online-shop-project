from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import product , comment
# Register your models here.

@admin.register(product)
class productAdmin(ModelAdmin):
    list_display=['title','des','price','datetime_add','image']
    
@admin.register(comment) 
class CommentAdmin(ModelAdmin):
    list_display=['text','rate','user','product','datetime_add','active']