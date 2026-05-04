from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm


def register(request):
    """
    Handle new user registration.

    GET  : render an empty RegisterForm.
    POST : validate the form, create the CustomUser with role set directly,
           log them in, then redirect to the home page.
    """
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.role = form.cleaned_data['role']   # stored directly on CustomUser
            user.save()

            login(request, user)
            return redirect('home')

    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    """
    Handle user login.

    After credentials are validated, check whether the account is an admin
    (is_staff / is_superuser). If so, block the login and show an error —
    admins must use /admin instead.
    """
    if request.user.is_authenticated:
        return redirect('home')

    error_message = None

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            # Step 2: Block admin accounts from the normal login page
            if user.is_staff or user.is_superuser:
                error_message = "Admin accounts must login from /admin"
            else:
                login(request, user)
                return redirect('home')

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {
        'form':          form,
        'error_message': error_message,
    })


def user_logout(request):
    """Log the current user out and redirect to the home page."""
    logout(request)
    return redirect('home')
