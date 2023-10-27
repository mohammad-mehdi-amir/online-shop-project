from django.shortcuts import render
from .forms import AddOrderForm
from cart.cart import Cart
from.models import order_item
from django.contrib import messages
from django.utils.translation import gettext as _
def order_create(request):
    cart=Cart(request)
    order_form=AddOrderForm()
    
    if request.method == 'POST':
        order_form=AddOrderForm(request.POST)
        
        if order_form.is_valid():
            if len(cart)!=0:
                
                order_obj =order_form.save(commit=False)
                order_obj.user=request.user
                order_obj.save()
                messages.success(request,_('your order has been registered'))
                
                for item in cart:
                    product=item['product_object']
                    order_item.objects.create(
                        order=order_obj,
                        product=product,
                        quantity=item['quantity'],
                        price=product.price,
                    )
                cart.clear()
            else:
                messages.error(request,_('your cart is empty'))
                
                
            
            
            
        else:
            messages.error(request,_('your order has not been registered, please try again'))
    else:
        order_form=AddOrderForm()
    return render(request,'orders/order_create.html',{
        'form':order_form,
    })
    