from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'delivery'

urlpatterns = [
    path('list/', login_required(views.PostDeliveryPackListView.as_view()), name='post_list'),
    path('<int:pk>/', login_required(views.delivery_pack_detail), name='detail'),
    path('list-c/', login_required(views.CustomerDeliveryPackListView.as_view()), name='customer_list'),
    path('c/<int:pk>/', login_required(views.CustomerPackDetailView.as_view()), name='customer_detail'),
]
