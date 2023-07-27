from django.shortcuts import render
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
    paginate_by = 4
    template_name = 'products/list_product.html'
    context_object_name = 'products'


# class ProductDetailView(DetailView):
#     model = product
#     template_name = "products/detail_product.html"
#     context_object_name = 'products'



def product_detail_view(request, pk):
    product1 = get_object_or_404(product, pk=pk)
    product_comments = product1.comments.all()
    
    if request.method == "POST":
        comment_form=commentForm(request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.product=product1
            new_comment.user=request.user
            new_comment.save()
            comment_form=commentForm()
    
    else:
        comment_form=commentForm()
        
    
    return render(request, "products/detail_product.html", {'products': product1, 'comments': product_comments,'form':comment_form})
