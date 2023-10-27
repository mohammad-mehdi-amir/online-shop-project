from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Customuser
# Register your models here.

@admin.register(Customuser)
class CustomuserAdmin(ModelAdmin):
    list_display=['username']
    