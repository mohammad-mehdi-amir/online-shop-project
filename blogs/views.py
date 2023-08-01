from django.shortcuts import render
from  django.urls import reverse_lazy
from .forms import new_blog_form
from django.views import generic
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import blog

class BlogListView(generic.ListView):
    model=blog
    template_name='blogs/blog_list.html'
    context_object_name='blogs'
    
class BlogDetailView(generic.DetailView):
    model=blog
    template_name='blogs/blog_detail.html'
    context_object_name='blog'
    
class BlogEditView(LoginRequiredMixin,generic.UpdateView):
    model=blog
    form_class=new_blog_form
    template_name='blogs/blog_edit.html'

    