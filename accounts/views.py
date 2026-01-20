from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Redirect theo role
            if user.role == 'recruiter':
                return redirect('recruiter_dashboard')
            elif user.role == 'candidate':
                return redirect('candidate_dashboard')
            else:
                logout(request)
                messages.error(request, 'Invalid role')
                return redirect('login')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def recruiter_dashboard(request):
    if request.user.role != 'recruiter':
        messages.error(request, 'Access denied')
        return redirect('candidate_dashboard' if request.user.role == 'candidate' else 'login')
    
    return render(request, 'accounts/recruiter_dashboard.html')


@login_required
def candidate_dashboard(request):
    if request.user.role != 'candidate':
        messages.error(request, 'Access denied')
        return redirect('recruiter_dashboard' if request.user.role == 'recruiter' else 'login')
    
    return render(request, 'accounts/candidate_dashboard.html')
