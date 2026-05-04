from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden
from accounts.decorators import recruiter_required, applicant_required
from .models import JobPost, Application
from .forms import JobPostForm, ApplicationForm


# ---------------------------------------------------------------------------
# Public views — require login, open to both roles
# ---------------------------------------------------------------------------

@login_required(login_url='/accounts/login/')
def job_list(request):
    """
    Blog-style listing of all job posts. Accessible to any logged-in user.

    GET parameters:
        q    — keyword searched across title, description, and tags
        tag  — filter to posts that contain this exact tag
        page — pagination page number (5 posts per page)
    """
    query      = request.GET.get('q',   '').strip()
    active_tag = request.GET.get('tag', '').strip().lower()

    jobs = JobPost.objects.select_related('recruiter').all()

    if query:
        jobs = jobs.filter(
            Q(title__icontains=query)       |
            Q(description__icontains=query) |
            Q(tags__icontains=query)
        )

    if active_tag:
        jobs = jobs.filter(tags__icontains=active_tag)

    all_raw_tags = JobPost.objects.values_list('tags', flat=True)
    tag_cloud = sorted({
        t.strip().lower()
        for raw in all_raw_tags
        for t in raw.split(',')
        if t.strip()
    })

    paginator = Paginator(jobs, 5)
    page_obj  = paginator.get_page(request.GET.get('page', 1))

    return render(request, 'jobs/job_list.html', {
        'page_obj':   page_obj,
        'query':      query,
        'active_tag': active_tag,
        'tag_cloud':  tag_cloud,
    })


@login_required(login_url='/accounts/login/')
def job_detail(request, job_id):
    """
    Show full details of a job post.
    Passes 'already_applied' flag so the template can show the right button state.
    """
    job = get_object_or_404(JobPost, id=job_id)

    already_applied = False
    if request.user.role == 'applicant':
        already_applied = Application.objects.filter(
            job=job, applicant=request.user
        ).exists()

    return render(request, 'jobs/job_detail.html', {
        'job':             job,
        'already_applied': already_applied,
    })


# ---------------------------------------------------------------------------
# Applicant-only views
# ---------------------------------------------------------------------------

@applicant_required
def apply_job(request, job_id):
    """
    Allow an applicant to apply to a job by uploading their CV (PDF).
    Duplicate applications redirect silently to job detail.
    """
    job = get_object_or_404(JobPost, id=job_id)

    if Application.objects.filter(job=job, applicant=request.user).exists():
        return redirect('jobs:job_detail', job_id=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            application           = form.save(commit=False)
            application.job       = job
            application.applicant = request.user
            application.save()
            return redirect('jobs:job_detail', job_id=job_id)

    else:
        form = ApplicationForm()

    return render(request, 'jobs/apply_job.html', {'form': form, 'job': job})


# ---------------------------------------------------------------------------
# Recruiter-only views
# ---------------------------------------------------------------------------

@recruiter_required
def create_job(request):
    """Allow a recruiter to create a new job post."""
    if request.method == 'POST':
        form = JobPostForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.recruiter = request.user
            job.save()
            return redirect('jobs:recruiter_jobs')

    else:
        form = JobPostForm()

    return render(request, 'jobs/create_job.html', {'form': form})


@recruiter_required
def edit_job(request, job_id):
    """
    Allow a recruiter to edit one of their own job posts.
    Returns 404 if the post does not belong to the current user.
    """
    job = get_object_or_404(JobPost, id=job_id, recruiter=request.user)

    if request.method == 'POST':
        form = JobPostForm(request.POST, instance=job)

        if form.is_valid():
            form.save()
            return redirect('jobs:recruiter_jobs')

    else:
        form = JobPostForm(instance=job)

    return render(request, 'jobs/edit_job.html', {'form': form, 'job': job})


@recruiter_required
def recruiter_jobs(request):
    """
    Recruiter dashboard: list only the posts created by the current recruiter.

    GET parameters:
        q    — keyword to search across title and tags (case-insensitive)
        sort — 'new' (default) → newest first | 'old' → oldest first
    """
    query = request.GET.get('q', '').strip()
    sort  = request.GET.get('sort', 'new')

    jobs = JobPost.objects.filter(recruiter=request.user)

    if query:
        jobs = jobs.filter(
            Q(title__icontains=query) | Q(tags__icontains=query)
        )

    if sort == 'old':
        jobs = jobs.order_by('created_at')
    else:
        jobs = jobs.order_by('-created_at')

    return render(request, 'jobs/recruiter_jobs.html', {
        'jobs':  jobs,
        'query': query,
        'sort':  sort,
    })


@recruiter_required
def view_applicants(request, job_id):
    """
    Show all CV applications submitted for one of the recruiter's job posts.

    CV access protection: get_object_or_404 with recruiter=request.user
    ensures a recruiter can only view applicants for their own jobs.
    """
    job          = get_object_or_404(JobPost, id=job_id, recruiter=request.user)
    applications = Application.objects.filter(job=job).select_related('applicant')

    return render(request, 'jobs/applicants_list.html', {
        'job':          job,
        'applications': applications,
    })


# ---------------------------------------------------------------------------
# Applicant — My Applications dashboard
# ---------------------------------------------------------------------------

@applicant_required
def my_applications(request):
    """List all applications submitted by the logged-in applicant."""
    applications = (
        Application.objects
        .filter(applicant=request.user)
        .select_related('job', 'job__recruiter')
        .order_by('-created_at')
    )
    return render(request, 'jobs/my_applications.html', {
        'applications': applications,
    })


@applicant_required
def view_my_cv(request, application_id):
    """Redirect the applicant to their own uploaded CV file."""
    application = get_object_or_404(Application, id=application_id)
    if application.applicant != request.user:
        return HttpResponseForbidden("You do not have permission to view this CV.")
    return redirect(application.cv_file.url)


@applicant_required
def withdraw_application(request, application_id):
    """Delete the applicant's own application and return to My Applications."""
    application = get_object_or_404(Application, id=application_id)
    if application.applicant != request.user:
        return HttpResponseForbidden("You do not have permission to withdraw this application.")
    if request.method == 'POST':
        application.delete()
    return redirect('jobs:my_applications')
