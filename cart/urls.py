from django.urls import path

from cart import views

app_name = 'cart'

urlpatterns = [
    path('', views.detail, name='detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('minus/<int:product_id>/', views.cart_minus, name='cart_minus'),
    path('plus/<int:product_id>/', views.cart_plus, name='cart_plus'),
]
