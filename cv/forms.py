from django import forms
from .models import CV


class CVUploadForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['file']
        widgets = {
            'file': forms.FileInput(attrs={'accept': '.pdf'})
        }
    
    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            if not file.name.endswith('.pdf'):
                raise forms.ValidationError('Only PDF files are allowed.')
        return file
