from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('panel/', include('panel.urls')),
    path('cashier/', include('cashier.urls')),
    path('kitchen/', include('kitchen.urls')),
]
