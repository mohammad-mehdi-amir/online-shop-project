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


class ProductListView(ListView):
    model = product
    paginate_by = 4
    template_name = 'products/list_product.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = product
    template_name = "products/detail_product.html"
    context_object_name = 'products'
