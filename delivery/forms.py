from django import forms
from .models import DeliveryPack


class PostDeliveryForm(forms.ModelForm):
    class Meta:
        model = DeliveryPack
        fields = ('post_tracking_code', 'is_post_delivered')
