from django.contrib import messages
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from accounts.forms import UserAddressForm

# Create your views here.
from django.views.decorators.http import require_POST
from django.utils import timezone
# from suds import Client

from cart.utils.cart import Cart
from order.models import Order, OrderItem


@login_required()
def order_create(request):
    cart = Cart(request)
    order = Order.objects.create(user=request.user)
    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], quantity=item['quantity'])
    cart.clear()
    return redirect('order:detail', order.id)


class OrderDetailView(generic.DetailView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderListView(generic.ListView):
    context_object_name = 'orders'
    template_name = 'order/order_list.html'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address_form'] = UserAddressForm(self.request.user)
        return context


@login_required()
def payment(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if order.user != request.user:
        raise Http404
    context = {'user': request.user, 'price': order.get_total_price, 'address': request.POST['address']}
    return render(request, 'order/payment.html', context)
