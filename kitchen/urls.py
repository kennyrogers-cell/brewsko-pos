from django.urls import path
from . import views

app_name = 'kitchen'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('orders/', views.get_orders, name='get_orders'),
    path('orders/<int:pk>/update/', views.update_order_status, name='update_order'),
]
