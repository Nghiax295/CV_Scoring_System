from django.http import HttpResponse
from django.shortcuts import redirect
from functools import wraps


def role_required(required_role):
    """
    Decorator kiểm tra role của user.
    Nếu user chưa login → redirect về login
    Nếu role không khớp → 403 Forbidden
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            # Kiểm tra user đã login chưa
            if not request.user.is_authenticated:
                return redirect('login')
            
            # Kiểm tra role
            if request.user.role != required_role:
                return HttpResponse("Forbidden", status=403)
            
            # Cho phép vào view
            return view_func(request, *args, **kwargs)
        
        return wrapper
    return decorator
