from django.db import models
from accounts.models import User
from panel.models import MenuItem


class Order(models.Model):
    TYPE_CHOICES = [('dine-in', 'Dine-In'), ('to-go', 'To-Go')]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    PAYMENT_CHOICES = [('cash', 'Cash'), ('gcash', 'GCash')]

    order_number = models.CharField(max_length=20, unique=True)
    order_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='dine-in')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    cashier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='orders')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES, null=True, blank=True)
    amount_received = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    reference_number = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.order_number}"

    @property
    def change(self):
        if self.amount_received and self.total:
            return float(self.amount_received) - float(self.total)
        return 0

    def save(self, *args, **kwargs):
        if not self.order_number:
            last = Order.objects.order_by('-id').first()
            num = (last.id + 1) if last else 1
            self.order_number = f"ORD-{num:03d}"
        super().save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.SET_NULL, null=True)
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    serving_style = models.CharField(max_length=50, blank=True)
    size = models.CharField(max_length=20, blank=True)
    temperature = models.CharField(max_length=20, blank=True)
    addons = models.JSONField(default=list)

    def __str__(self):
        return f"{self.quantity}x {self.item_name}"

    def customizations_display(self):
        parts = []
        if self.serving_style:
            parts.append(self.serving_style)
        if self.size:
            parts.append(self.size)
        if self.temperature:
            parts.append(self.temperature)
        if self.addons:
            parts.extend(self.addons)
        return ', '.join(parts)
