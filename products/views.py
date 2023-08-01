from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import product
from .form import *
from django.views.generic import *
from django.urls import reverse
from django.shortcuts import get_object_or_404
# Create your views here.


class NewProductView(CreateView):
    model = product
    form_class = new_product_form
    template_name = "products/new_proudct.html"


class ProductListView(ListView):
    model = product
    paginate_by = 8
    template_name = 'products/list_product.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = product
    template_name = "products/detail_product.html"
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['comment_form']=commentForm()
        return context


class CommentCreateView(CreateView):
    model= comment
    form_class=commentForm  
    
    def form_valid(self, form):
        obj=form.save(commit=False)
        obj.user=self.request.user
        product_id=int(self.kwargs['pk'])
        obj.product=get_object_or_404(product,id=product_id)
        return super().form_valid(form)
    
    

    
# def product_detail_view(request, pk):
#     product1 = get_object_or_404(product, pk=pk)
#     product_comments = product1.comments.all()
    
#     if request.method == "POST":

#         comment_form=commentForm(request.POST)
#         if comment_form.is_valid():
#             new_comment=comment_form.save(commit=False)
#             new_comment.product=product1
#             new_comment.user=request.user
#             new_comment.save()
#             comment_form=commentForm()
#             return redirect(product1)
    
#     else:
#         comment_form=commentForm()
#         return render(request, "products/detail_product.html", {'products': product1, 'comments': product_comments,'form':comment_form})
