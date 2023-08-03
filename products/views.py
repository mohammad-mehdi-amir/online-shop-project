from django.forms.models import BaseModelForm
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from .models import product,comment
from .form import commentForm ,new_product_form
from cart.forms import AddToCartForm
from django.views.generic import *
from cart.cart import Cart
from django.utils.translation import gettext as _
# Create your views here.

def home_view(request):
    cart=Cart(request)
    return render(request,'home.html')

class NewProductView(CreateView):
    model = product
    form_class = new_product_form
    template_name = "products/new_proudct.html"


class ProductListView(ListView):
    model = product
    paginate_by = 20
    template_name = 'products/list_product.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = product
    template_name = "products/detail_product.html"
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['comment_form']=commentForm()
        context['add_to_cart_form']=AddToCartForm()
        return context


class CommentCreateView(CreateView):
    model= comment
    form_class=commentForm
    def form_valid(self, form):
        messages.success(self.request, _('your comment sended'))
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
