from django.contrib import admin

from django.urls import path,include

from .views import SingupView
from django.views import generic
urlpatterns = [
    path('singup/',SingupView.as_view(),name='singup'),
    path('',generic.TemplateView.as_view(template_name='home.html'),name='home'),
]
