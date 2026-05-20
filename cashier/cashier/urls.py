from django.urls import path
from . import views

app_name = 'cashier'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('order/', views.order, name='order'),
    path('order-statuses/', views.order_statuses, name='order_statuses'),
    path('submit/', views.submit_order, name='submit_order'),
]
