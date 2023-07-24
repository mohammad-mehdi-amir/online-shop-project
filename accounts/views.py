from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import generic
from .forms import CustomUserCreationForm

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.
# class SingupView(CreateView):
#     form_class=CustomUserCreationForm
#     template_name='registration/singup.html'
#     success_url=reverse_lazy('login')


class SingupView(generic.CreateView):
    form_class=CustomUserCreationForm
    template_name = "registration/singup.html"
    success_url=reverse_lazy('login')
    

