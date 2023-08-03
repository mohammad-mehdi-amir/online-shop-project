from django.contrib import admin

from django.urls import path,include

from .views import SingupView
from django.views import generic
urlpatterns = [
    path('singup/',SingupView.as_view(),name='singup'),
    
]
