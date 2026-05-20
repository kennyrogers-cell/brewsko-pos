from django.contrib import admin
from .models import MenuItem, InventoryItem, Addon

admin.site.register(MenuItem)
admin.site.register(InventoryItem)
admin.site.register(Addon)
