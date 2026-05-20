from functools import wraps
from django.shortcuts import redirect


def role_required(allowed_roles, login_url='login'):
    """Require the current user to have one of the allowed roles."""
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated or request.user.role not in allowed_roles:
                return redirect(login_url)
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


def serialize_items(queryset):
    """Convert a queryset of menu items to a JSON-safe list."""
    return [
        {
            'id': item.id,
            'name': item.name,
            'price': float(item.price),
            'category': item.category,
            'has_serving_style': item.has_serving_style,
            'has_size': item.has_size,
            'has_temperature': item.has_temperature,
        }
        for item in queryset
    ]
