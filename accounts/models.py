from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Custom user model that extends Django's AbstractUser.

    Adds a 'role' field to distinguish between:
        applicant  — a job seeker who uploads CVs and applies to jobs
        recruiter  — a company representative who posts jobs and reviews CVs

    Django Admin (is_staff / is_superuser) is NOT assigned a role here.
    Admins log in exclusively through /admin.
    """

    ROLE_CHOICES = [
        ('recruiter', 'Recruiter'),
        ('applicant', 'Applicant'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        blank=True,
        default='',
    )

    def __str__(self):
        return f"{self.username} ({self.role or 'admin'})"
