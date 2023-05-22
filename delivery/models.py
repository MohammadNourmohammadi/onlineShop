from django.db import models
from accounts.models import MyUser
from order.models import Order
from django.utils import timezone


class DeliveryPack(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='delivery_packs')
    zip_code = models.CharField(max_length=10)
    address_text = models.CharField(max_length=100)
    name_of_transferee = models.CharField(max_length=20)
    phone_of_transferee = models.CharField(max_length=15)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    post_tracking_code = models.CharField(max_length=24, null=True)
    is_post_delivered = models.BooleanField(default=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='delivery_pack')
    created = models.DateTimeField(default=timezone.now)
    authority = models.CharField(max_length=100)
    ref_id = models.IntegerField(default=0)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name_of_transferee



