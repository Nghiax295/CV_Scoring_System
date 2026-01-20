from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.decorators import role_required
from .forms import CVUploadForm
from .models import CV


@login_required
@role_required('candidate')
def upload_cv(request):
    if request.method == 'POST':
        form = CVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.owner = request.user
            cv.save()
            messages.success(request, 'CV uploaded successfully!')
            return redirect('my_cv_list')
    else:
        form = CVUploadForm()
    
    return render(request, 'cv/upload_cv.html', {'form': form})


@login_required
@role_required('candidate')
def my_cv_list(request):
    cvs = CV.objects.filter(owner=request.user).order_by('-uploaded_at')
    return render(request, 'cv/my_cv_list.html', {'cvs': cvs})
