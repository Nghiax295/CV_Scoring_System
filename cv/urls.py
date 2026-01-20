from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_cv, name='upload_cv'),
    path('my/', views.my_cv_list, name='my_cv_list'),
]
