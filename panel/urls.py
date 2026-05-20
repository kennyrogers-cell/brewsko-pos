from django.urls import path
from . import views

app_name = 'panel'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('menu/', views.manage_menu, name='menu'),
    path('menu/add/', views.add_menu_item, name='add_menu_item'),
    path('menu/<int:pk>/edit/', views.edit_menu_item, name='edit_menu_item'),
    path('menu/<int:pk>/delete/', views.delete_menu_item, name='delete_menu_item'),
    path('menu/<int:pk>/delete-achieved/', views.delete_achieved_menu_item, name='delete_achieved_menu_item'),
    path('menu/<int:pk>/restore/', views.restore_menu_item, name='restore_menu_item'),
    path('menu/<int:pk>/toggle/', views.toggle_menu_item, name='toggle_menu_item'),
    path('menu/<int:pk>/achieve/', views.achieve_menu_item, name='achieve_menu_item'),
    path('menu/<int:pk>/data/', views.get_menu_item_data, name='menu_item_data'),
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/add/', views.add_inventory_item, name='add_inventory_item'),
    path('inventory/<int:pk>/edit/', views.edit_inventory_item, name='edit_inventory_item'),
    path('inventory/<int:pk>/achieve/', views.achieve_inventory_item, name='achieve_inventory_item'),
    path('inventory/<int:pk>/delete/', views.delete_inventory_item, name='delete_inventory_item'),
    path('inventory/<int:pk>/delete-achieved/', views.delete_achieved_inventory_item, name='delete_achieved_inventory_item'),
    path('inventory/<int:pk>/restore/', views.restore_inventory_item, name='restore_inventory_item'),
    path('inventory/<int:pk>/data/', views.get_inventory_item_data, name='inventory_item_data'),
    path('security/', views.security, name='security'),
    path('security/user/add/', views.add_user, name='add_user'),
    path('security/user/<int:pk>/edit/', views.edit_user, name='edit_user'),
    path('security/user/<int:pk>/delete/', views.delete_user, name='delete_user'),
    path('security/user/<int:pk>/data/', views.get_user_data, name='user_data'),
]
