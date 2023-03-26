from django.shortcuts import render, get_object_or_404, redirect
from cart.forms import Add2CartForm
from cart.utils.cart import Cart
from shop.models import Product


def detail(request):
    cart = Cart(request)
    return render(request, template_name='cart/detail.html', context={'cart': cart})


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = Add2CartForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cart.add(product=product, quantity=data['quantity'])
    elif request.method == 'GET':
        cart.add(product=product, quantity=1)

    return redirect('cart:detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:detail')
