from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.decorators import role_required
from .forms import CVUploadForm
from .models import CV
from .services import extract_text_from_pdf, preprocess_text


@login_required
@role_required('candidate')
def upload_cv(request):
    if request.method == 'POST':
        form = CVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.owner = request.user
            cv.save()
            
            # Trích xuất text từ PDF
            extracted_text = extract_text_from_pdf(cv)
            if extracted_text:
                cv.extracted_text = extracted_text
                
                # Tiền xử lý text
                cleaned_text = preprocess_text(extracted_text)
                if cleaned_text:
                    cv.cleaned_text = cleaned_text
                
                cv.save(update_fields=['extracted_text', 'cleaned_text'])
            
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


@login_required
@role_required('recruiter')
def recruiter_cv_list(request):
    cvs = CV.objects.select_related('owner').order_by('-uploaded_at')
    return render(request, 'cv/recruiter_cv_list.html', {'cvs': cvs})
