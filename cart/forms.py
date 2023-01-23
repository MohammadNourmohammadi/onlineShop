from django import forms


class Add2CartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, widget=forms.NumberInput(), label='تعداد')