from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('address/', login_required(views.AddressListView.as_view()), name='address_list'),
    path('address/<int:pk>/', login_required(views.AddressDetailView.as_view()), name='address_detail'),
    path('address/create', views.create_address, name='create_Address'),
    path('password-reset/', views.CustomPasswordResetView.as_view(),
         name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         views.CustomPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset-done/',
         views.CustomPasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password-reset-complete/',
         views.CustomPasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
