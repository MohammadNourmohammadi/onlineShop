from django.shortcuts import render, get_object_or_404, redirect
from order.models import Order
from .models import DeliveryPack
from django.views import generic
from django.http import Http404
from .forms import PostDeliveryForm


def create_delivery_pack(order: Order):
    delivery_pack = DeliveryPack.objects.create(user=order.user, zip_code=order.address.zip_code,
                                                address_text=order.address.address_text,
                                                name_of_transferee=order.address.name_of_transferee,
                                                phone_of_transferee=order.address.phone_of_transferee,
                                                state=order.address.state, city=order.address.city,
                                                authority=order.authority, order=order)
    delivery_pack.save()


class PostDeliveryPackListView(generic.ListView):
    model = DeliveryPack
    context_object_name = 'delivery_packs'
    template_name = 'delivery/post_delivery_list.html'

    def get_queryset(self):
        if self.request.user.is_delivery_man:
            if 'is_post' in self.request.GET.keys():
                return DeliveryPack.objects.filter(is_post_delivered=True)
            return DeliveryPack.objects.filter(is_post_delivered=False)
        return None


def delivery_pack_detail(request, pk):
    if not request.user.is_delivery_man:
        raise Http404

    if request.method == 'POST':
        delivery_pack = get_object_or_404(DeliveryPack, pk=pk)
        delivery_pack.post_tracking_code = request.POST['post_tracking_code']
        if 'is_post_delivered' in request.POST.keys():
            delivery_pack.is_post_delivered = True
        else:
            delivery_pack.is_post_delivered = False
        delivery_pack.save()
        return redirect('delivery:not-post')
    else:
        form = PostDeliveryForm()
        delivery_pack = get_object_or_404(DeliveryPack, pk=pk)
        return render(request, 'delivery/delivery_pack_detail.html', {'form': form,
                                                                      'delivery_pack': delivery_pack}, )
