from django import forms
from .models import CustomUser


class RegisterForm(forms.ModelForm):
    """
    Registration form for new users.

    Targets CustomUser directly, so the 'role' field is saved
    on the user object itself (no separate Profile model needed).

    Validation:
        - username  : unique (enforced automatically by ModelForm)
        - email     : required + unique (custom clean_email)
        - password  : minimum 6 characters (custom clean_password)
        - role      : must be 'applicant' or 'recruiter'
    """

    password = forms.CharField(
        label="Password",
        min_length=6,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}),
    )

    role = forms.ChoiceField(
        label="Role",
        choices=CustomUser.ROLE_CHOICES,
    )

    class Meta:
        model  = CustomUser
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter username'}),
            'email':    forms.EmailInput(attrs={'placeholder': 'Enter email'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required.")
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and len(password) < 6:
            raise forms.ValidationError("Password must be at least 6 characters.")
        return password
