from django import forms
from .models import JobPost, Application


class JobPostForm(forms.ModelForm):
    """
    Form for creating and editing a JobPost.

    The 'recruiter' and 'created_at' fields are excluded because:
        - recruiter  is assigned automatically from request.user in the view
        - created_at is set automatically by auto_now_add=True on the model
    """

    class Meta:
        model  = JobPost
        fields = ['title', 'description', 'requirement', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'e.g. Backend Django Developer',
            }),
            'description': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Describe the role and responsibilities...',
            }),
            'requirement': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'List the required skills and qualifications...',
            }),
            'tags': forms.TextInput(attrs={
                'placeholder': 'e.g. Python, Django, REST API',
            }),
        }
        labels = {
            'tags': 'Tags (comma-separated)',
        }


class ApplicationForm(forms.ModelForm):
    """
    Form for submitting a job application with a CV upload.

    Only the cv_file field is exposed; job and applicant are set in the view.
    PDF-only validation is enforced in clean_cv_file().
    """

    class Meta:
        model  = Application
        fields = ['cv_file']
        labels = {
            'cv_file': 'Upload your CV (PDF only)',
        }

    def clean_cv_file(self):
        """Reject any upload that is not a .pdf file."""
        file = self.cleaned_data.get('cv_file')
        if file:
            if not file.name.lower().endswith('.pdf'):
                raise forms.ValidationError("Only PDF files are accepted.")
        return file
