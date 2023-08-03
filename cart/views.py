from django.shortcuts import render, get_object_or_404, redirect
from cart.cart import Cart
from .forms import AddToCartForm
from products.models import product
from django.contrib import messages
from django.utils.translation import gettext as _
# Create your views here.


def cart_detail_view(request):
    cart = Cart(request)

    for item in cart:
        item['form'] = AddToCartForm(initial={
            'quantity': item['quantity'],
            'inplace': True,
        })
        
    return render(request, 'cart/cart_detail.html', {
        'cart': cart
    })


def add_to_cart_view(request, product_id):
    cart = Cart(request)

    Product1 = get_object_or_404(product, id=product_id)

    form = AddToCartForm(request.POST)

    if form.is_valid():
        claened_date = form.cleaned_data
        quaintity = claened_date['quantity']
        add_or_replace = claened_date['inplace']
        cart.add(Product1, quaintity,add_or_replace=add_or_replace)
    messages.success(request,Product1.title+ _(' added to cart successfuly'))
    return redirect('cart:cart_detail')


def remove_cart(request, product_id):
    cart = Cart(request)

    Product1 = get_object_or_404(product, id=product_id)

    cart.remove(Product1)
    messages.error(request,Product1.title+ _(' remove form cart successfully'))
    return redirect('cart:cart_detail')


def clean_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart_detail')
