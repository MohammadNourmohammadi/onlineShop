from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import UserLoginForm, UserRegistrationForm
from accounts.models import MyUser


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
                return redirect('shop:index')
            else:
                messages.error(request, 'رمز ها یکسان نیستند', 'danger')

    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
