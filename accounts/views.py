from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import UserLoginForm, UserRegistrationForm, UserAddressForm
from accounts.models import MyUser
from django.views import generic
from .models import UserAddress
from django.contrib.auth.decorators import login_required
from accounts import email_service
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView
from django.urls import reverse_lazy


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, email=data['email'], password=data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'با موفقیت وارد شدید', 'success')
                return redirect('shop:index')
            else:
                messages.error(request, 'ایمیل یا رمز اشتباه است', 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'با موفقیت خارج شدید', 'success')
    return redirect('shop:index')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data['password1'] and data['password2'] and data['password1'] == data['password2']:
                user = MyUser.objects.create_user(email=data['email'], password=data['password1'],
                                                  first_name=data['first_name'], last_name=data['last_name'],
                                                  phone_number=data['phone_number'], )
                login(request, user)
                messages.success(request, 'با موفقیت ثبت نام شدید', 'success')
                email_service.welcome_email_new_user(user)
                return redirect('shop:index')
            else:
                messages.error(request, 'رمز ها یکسان نیستند', 'danger')

    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


class AddressListView(generic.ListView):
    context_object_name = 'addresses'
    template_name = 'accounts/address_list.html'

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)


class AddressDetailView(generic.DetailView):
    context_object_name = 'address'
    template_name = 'accounts/address_detail.html'

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)


@login_required()
def create_address(request):
    if request.method == 'POST':
        if request.user.get_size_address() >= 5:
            messages.error(request, 'نمی توان بیشتر از ۵ تا آدرس ساخت', 'danger')
            return redirect('accounts:address_list')
        form = UserAddressForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            address = UserAddress.objects.create(user=request.user, name=data['name'],
                                                 name_of_transferee=data['name_of_transferee'],
                                                 phone_of_transferee=data['phone_of_transferee'], city=data['city'],
                                                 state=data['state'], address_text=data['address_text'],
                                                 zip_code=data['zip_code'])
            address.save()
            return redirect('accounts:address_list')

    else:
        form = UserAddressForm()
    return render(request, 'accounts/address_create.html', {'form': form})


class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'accounts/email_templates/password_reset_email.html'
    template_name = 'accounts/password_reset.html'
    success_url = reverse_lazy('accounts:password_reset_done')


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
