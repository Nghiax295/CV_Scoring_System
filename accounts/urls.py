from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('recruiter/dashboard/', views.recruiter_dashboard, name='recruiter_dashboard'),
    path('candidate/dashboard/', views.candidate_dashboard, name='candidate_dashboard'),
]
