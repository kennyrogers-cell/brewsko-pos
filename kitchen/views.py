from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone

from brewsko_pos.utils import role_required
from cashier.models import Order


@role_required(['kitchen', 'admin'])
def dashboard(request):
    return render(request, 'kitchen/dashboard.html')


@role_required(['kitchen', 'admin'])
def get_orders(request):
    active_orders = Order.objects.filter(
        status__in=['pending', 'preparing', 'ready']
    ).prefetch_related('items').order_by('created_at')

    orders_data = [
        {
            'id': order.id,
            'order_number': order.order_number,
            'order_type': order.get_order_type_display(),
            'status': order.status,
            'created_at': timezone.localtime(order.created_at).strftime('%I:%M %p'),
            'items': [
                {
                    'name': item.item_name,
                    'quantity': item.quantity,
                    'price': float(item.subtotal),
                    'customizations': item.customizations_display(),
                }
                for item in order.items.all()
            ],
        }
        for order in active_orders
    ]

    today = timezone.localdate()
    stats = {
        'pending': Order.objects.filter(status='pending').count(),
        'preparing': Order.objects.filter(status='preparing').count(),
        'ready': Order.objects.filter(status='ready').count(),
        'total': Order.objects.filter(created_at__date=today).count(),
    }

    return JsonResponse({'orders': orders_data, 'stats': stats})


@role_required(['kitchen', 'admin'])
def update_order_status(request, pk):
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Invalid request method.'})

    order = get_object_or_404(Order, pk=pk)
    transitions = {
        'pending': 'preparing',
        'preparing': 'ready',
        'ready': 'completed',
    }
    if order.status in transitions:
        order.status = transitions[order.status]
        order.save()

    return JsonResponse({'success': True, 'new_status': order.status})
