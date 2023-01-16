from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from .models import MyUser


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'first_name', 'last_name', 'phone_number',)

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
        fields = ('email', 'password', 'first_name', 'last_name', 'phone_number',)

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
