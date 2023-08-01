from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import *
from .models import Customuser
# Register your models here.


@admin.register(Customuser)
class CustomUserAdmin(UserAdmin):
    model = Customuser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email', 'username','is_staff')
