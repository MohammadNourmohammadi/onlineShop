from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'delivery'

urlpatterns = [
    path('list/', login_required(views.PostDeliveryPackListView.as_view()), name='post_list'),
    path('<int:pk>/', login_required(views.delivery_pack_detail), name='detail'),
]
