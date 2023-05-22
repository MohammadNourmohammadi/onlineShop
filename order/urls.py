from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'order'

urlpatterns = [
    path('create/', login_required(views.order_create), name='order_create'),
    path('<int:pk>/', login_required(views.OrderDetailView.as_view()), name='detail'),
    path('', login_required(views.OrderListView.as_view()), name='order_list'),
    path('payment/<int:order_id>/', views.payment, name='payment'),
    path('delete/<int:pk>', views.delete_order, name='delete_order'),
    path('verify/', views.verify, name='verify')

]
