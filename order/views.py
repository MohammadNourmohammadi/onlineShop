from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from delivery.views import create_delivery_pack
from accounts.models import UserAddress
from cart.utils.cart import Cart
from order.models import Order, OrderItem
from django.views.decorators.http import require_POST
from order.sms_service import send_sms_success_payment
from .zarinpal import send_request, verify_pay


@require_POST
def order_create(request):
    cart = Cart(request)
    if cart.size_cart() == 0:
        messages.error(request, 'سبد شما خالی است', 'danger')
        return redirect('cart:detail')
    if request.user.get_size_open_orders() >= 5:
        messages.error(request, 'نمی توان بیشتر از ۵ تا سفارش باز داشت', 'danger')
        return redirect('order:order_list')
    order = Order.objects.create(user=request.user)
    if cart.get_total_price() < 390000:
        order.post_cost = 35000
        # order.post_cost = 20000 if request.POST['post_method'] == 'post_tehran' else 30000
        order.save()
    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], quantity=item['quantity'])
    cart.clear()
    messages.success(request, 'فاکتور شما ساخته شد و آماده پرداخت می باشد.', 'success')
    return redirect('order:order_list')


class OrderDetailView(generic.DetailView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, is_paid=False)


class OrderListView(generic.ListView):
    context_object_name = 'orders'
    template_name = 'order/order_list.html'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, is_paid=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['addresses'] = self.request.user.address.all()
        return context


@login_required()
def payment(request, order_id):
    if request.method != 'POST':
        raise Http404
    order = get_object_or_404(Order, pk=order_id)
    if order.user != request.user:
        raise Http404
    if 'address' not in request.POST:
        messages.error(request, 'آدرس باید انتخاب شود', 'danger')
        return redirect('order:order_list')
    address = get_object_or_404(UserAddress, pk=request.POST['address'])
    response = send_request(order.get_total_price, f"{request.user.last_name} سفارش ")
    if response['status']:
        order.authority = response['authority']
        order.address = address
        order.save()
        return redirect(response['url'])
    messages.error(request, 'پرداخت با موفقیت انجام نشد لطفا دوباره تلاش کنید', 'danger')
    print(response['code'])
    return redirect('order:order_list')
    # order.is_paid = True
    # create_delivery_pack(order)
    # send_sms_success_payment.delay(order.address.phone_of_transferee, order.address.name_of_transferee)
    # context = {'user': request.user, 'price': order.get_total_price, 'address': request.POST['address']}
    # return render(request, 'order/payment.html', context)


def verify(request):
    if 'Authority' not in request.GET:
        raise Http404
    auth = request.GET['Authority']
    order = get_object_or_404(Order, authority=auth)
    response = verify_pay(auth, order.get_total_price)
    if response['status']:
        order.is_paid = True
        order.save()
        create_delivery_pack(order, response['RefID'])
        send_sms_success_payment.delay(order.address.phone_of_transferee, order.address.name_of_transferee)
    else:
        print(response['code'])
    return redirect('delivery:customer_list')


@login_required()
def delete_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if order.user != request.user:
        raise Http404
    if order.is_paid:
        messages.error(request, 'نمی توان سفارش پرداخت شده را حذف کرد', 'danger')
        return redirect('order:order_list')
    order.delete()
    messages.success(request, "سفارش با موفقیت حذف شد")
    return redirect('order:order_list')
