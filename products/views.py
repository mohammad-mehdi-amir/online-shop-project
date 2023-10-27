from django.forms.models import BaseModelForm
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from django.views.generic import *
from django.utils.translation import gettext as _

from .models import product,comment
from .form import commentForm ,new_product_form
from products import form
from likes.models import like

from cart.forms import AddToCartForm
from cart.cart import Cart
# Create your views here.

def home_view(request):
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
    def get_context_data(self,*args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args,**kwargs)
        context['likes'] = like.objects.all()
        return context


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
    
    
def search_view(request):
    word=request.POST['popup_search']
    products1 = product.objects.filter(title__contains=word).filter(status=True)
    return render(request,'products/list_product.html',{'products':products1})
    
