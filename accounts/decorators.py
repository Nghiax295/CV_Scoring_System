from functools import wraps
from django.http import HttpResponseForbidden
from django.shortcuts import redirect


def recruiter_required(view_func):
    """
    Decorator that restricts a view to authenticated recruiters only.

    - Unauthenticated users → redirect to login page.
    - Authenticated non-recruiters → 403 Forbidden.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        if request.user.role != 'recruiter':
            return HttpResponseForbidden("Access denied. Recruiters only.")
        return view_func(request, *args, **kwargs)
    return wrapper


def applicant_required(view_func):
    """
    Decorator that restricts a view to authenticated applicants only.

    - Unauthenticated users → redirect to login page.
    - Authenticated non-applicants → 403 Forbidden.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        if request.user.role != 'applicant':
            return HttpResponseForbidden("Access denied. Applicants only.")
        return view_func(request, *args, **kwargs)
    return wrapper
