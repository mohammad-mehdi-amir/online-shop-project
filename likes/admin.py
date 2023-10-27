from django.contrib import admin
from .models import like
# Register your models here.
@admin.register(like)
class LikeAdmin(admin.ModelAdmin):
    list_display=['user','product']