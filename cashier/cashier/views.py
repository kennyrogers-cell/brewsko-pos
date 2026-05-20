from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone
import json

from brewsko_pos.utils import role_required, serialize_items
from panel.models import MenuItem, FOOD_CATEGORIES, DRINK_CATEGORIES
from .models import Order, OrderItem


def get_category_groups(categories):
    groups = {}
    for category in categories:
        items = MenuItem.objects.filter(category=category, status='available')
        if items.exists():
            groups[category] = serialize_items(items)
    return groups


@role_required(['cashier', 'admin'])
def welcome(request):
    return render(request, 'cashier/welcome.html')


@role_required(['cashier', 'admin'])
def order(request):
    food_categories = get_category_groups(FOOD_CATEGORIES)
    drink_categories = get_category_groups(DRINK_CATEGORIES)

    context = {
        'food_categories': json.dumps(food_categories),
        'drink_categories': json.dumps(drink_categories),
        'food_cat_names': json.dumps(list(food_categories.keys())),
        'drink_cat_names': json.dumps(list(drink_categories.keys())),
    }
    return render(request, 'cashier/order.html', context)


@role_required(['cashier', 'admin'])
def order_statuses(request):
    active_orders = Order.objects.filter(status__in=['pending', 'preparing', 'ready']).order_by('-created_at')[:8]
    notifications = [
        {
            'order_number': order.order_number,
            'order_type': order.get_order_type_display(),
            'status': order.status,
            'created_at': timezone.localtime(order.created_at).strftime('%I:%M %p'),
        }
        for order in active_orders
    ]

    stats = {
        'pending': Order.objects.filter(status='pending').count(),
        'preparing': Order.objects.filter(status='preparing').count(),
        'ready': Order.objects.filter(status='ready').count(),
        'total': Order.objects.filter(status__in=['pending', 'preparing', 'ready']).count(),
    }

    return JsonResponse({'notifications': notifications, 'stats': stats})


@role_required(['cashier', 'admin'])
def submit_order(request):
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Invalid request method.'})

    data = json.loads(request.body)
    items = data.get('items', [])
    payment_method = data.get('payment_method')
    amount_received = data.get('amount_received', 0)
    reference_number = data.get('reference_number', '')
    order_type = data.get('order_type', 'dine-in')

    if not items:
        return JsonResponse({'success': False, 'error': 'No items in order.'})

    total = sum(float(item.get('subtotal', 0)) for item in items)

    if payment_method == 'cash' and float(amount_received) < total:
        return JsonResponse({'success': False, 'error': 'Insufficient amount.'})

    order = Order.objects.create(
        order_type=order_type,
        cashier=request.user,
        total=total,
        payment_method=payment_method,
        amount_received=amount_received,
        reference_number=reference_number,
        status='pending',
    )

    order_items = []
    for item_data in items:
        menu_item = None
        menu_item_id = item_data.get('id')
        if menu_item_id:
            menu_item = MenuItem.objects.filter(pk=menu_item_id).first()

        order_item = OrderItem.objects.create(
            order=order,
            menu_item=menu_item,
            item_name=item_data.get('name', ''),
            quantity=item_data.get('quantity', 0),
            unit_price=item_data.get('unit_price', 0),
            subtotal=item_data.get('subtotal', 0),
            serving_style=item_data.get('serving_style', ''),
            size=item_data.get('size', ''),
            temperature=item_data.get('temperature', ''),
            addons=item_data.get('addons', []),
        )
        order_items.append(order_item)

    change = float(amount_received) - total if payment_method == 'cash' else 0

    return JsonResponse({
        'success': True,
        'order_number': order.order_number,
        'total': total,
        'payment_method': payment_method,
        'amount_received': float(amount_received),
        'change': change,
        'reference_number': reference_number,
        'order_type': order_type,
        'items': [
            {'name': item.item_name, 'quantity': item.quantity, 'subtotal': float(item.subtotal)}
            for item in order_items
        ],
        'created_at': order.created_at.strftime('%m/%d/%Y, %I:%M %p'),
    })
