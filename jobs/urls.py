from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    # /jobs/                  → all job posts (blog-style listing)
    path('', views.job_list, name='job_list'),

    # /jobs/create/           → recruiter creates a new post
    path('create/', views.create_job, name='create_job'),

    # /jobs/myjobs/           → recruiter dashboard
    path('myjobs/', views.recruiter_jobs, name='recruiter_jobs'),

    # /jobs/apply/<id>/       → applicant submits CV for a job
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),

    # /jobs/applicants/<id>/  → recruiter views all applicants for a job
    path('applicants/<int:job_id>/', views.view_applicants, name='view_applicants'),

    # /jobs/applications/                  → applicant's own application list
    path('applications/', views.my_applications, name='my_applications'),

    # /jobs/applications/<id>/cv/          → redirect to applicant's own CV file
    path('applications/<int:application_id>/cv/', views.view_my_cv, name='view_my_cv'),

    # /jobs/applications/<id>/withdraw/    → applicant withdraws their application
    path('applications/<int:application_id>/withdraw/', views.withdraw_application, name='withdraw_application'),

    # /jobs/<id>/             → job detail (dynamic, kept after concrete paths)
    path('<int:job_id>/', views.job_detail, name='job_detail'),

    # /jobs/edit/<id>/        → recruiter edits their own post
    path('edit/<int:job_id>/', views.edit_job, name='edit_job'),
]
