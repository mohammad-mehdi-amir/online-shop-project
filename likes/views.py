from django.shortcuts import render,get_object_or_404
from django.views import generic

from .models import like
from products.models import product 

class AddLike(generic.CreateView):
    model=like
    
from django.shortcuts import render,redirect
from .models import product, like



class LikeListView(generic.ListView):
    model = like
    paginate_by = 20
    template_name =  'likes/list_liked.html'
    context_object_name = 'products'



def add_like(request,pk):
    product_obj = product.objects.get(id=pk)
    like_obj, created = like.objects.get_or_create(
        user=request.user,
        product=product_obj
    )

    return render(request, 'likes/list_liked.html', {
        'products': like.objects.filter(user=request.user.id),
    })
    
def remove_like(request,pk):
    product_liked = get_object_or_404(like,product=pk) 
    product_liked.delete()
    
    return redirect('list_prodcut')