from django.shortcuts import render
from .models import product
from .form import new_product_form
from django.views.generic import *
from django.urls import reverse
# Create your views here.


class NewProductView(CreateView):
    model = product
    form_class = new_product_form
    template_name = "products/new_proudct.html"

