from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from .models import MyUser, UserAddress


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'is_delivery_man')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise forms.ValidationError('passwords must match')
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'first_name', 'last_name', 'phone_number', 'is_delivery_man')

    def clean_password(self):
        return self.initial['password']


class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())


class UserRegistrationForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(), label='ایمیل')
    first_name = forms.CharField(widget=forms.TextInput(), max_length=20, label='نام')
    last_name = forms.CharField(widget=forms.TextInput(), max_length=20, label='نام خانوادگی')
    phone_number = forms.CharField(max_length=11, widget=forms.TextInput(), label='تلفن همراه')
    password1 = forms.CharField(widget=forms.PasswordInput(), label='رمز')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='تکرار رمز')


class ChoiceUserAddressForm(forms.Form):
    address = forms.ChoiceField(choices=(), label="آدرس")

    def __init__(self, user, *args, **kwargs):
        super(ChoiceUserAddressForm, self).__init__(*args, **kwargs)
        valid_address = UserAddress.objects.filter(user=user)
        self.fields['address'].choices = [(address.id, address) for address in valid_address]


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        exclude = ('user',)
        labels = {
            'name': 'اسم آدرس',
            'zip_code': 'کد پستی',
            'address_text': 'آدرس',
            'name_of_transferee': 'نام دریافت کننده',
            'phone_of_transferee': 'شماره دریافت کننده',
            'state': 'استان',
            'city': 'شهر',
        }

    def __init__(self, *args, **kwargs):
        super(UserAddressForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.initial['name'] = self.instance.name
            self.initial['zip_code'] = self.instance.zip_code
            self.initial['address_text'] = self.instance.address_text
            self.initial['name_of_transferee'] = self.instance.name_of_transferee
            self.initial['phone_of_transferee'] = self.instance.phone_of_transferee
            self.initial['state'] = self.instance.state
            self.initial['city'] = self.instance.city
