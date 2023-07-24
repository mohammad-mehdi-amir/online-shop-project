from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import product
# Register your models here.

@admin.register(product)
class productAdmin(ModelAdmin):
    list_display=['title','des','price','datetime_add','image']