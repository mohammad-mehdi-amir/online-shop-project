from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import blog
# Register your models here.

@admin.register(blog)
class blogAdmin(ModelAdmin):
    list_display=['title','text','author','datetime_add',]
    