from django.db import models
from django.conf import settings


class JobPost(models.Model):
    """
    Represents a job listing created by a recruiter.

    Uses settings.AUTH_USER_MODEL so the FK stays compatible
    with the custom CustomUser model.
    """

    title       = models.CharField(max_length=200)
    description = models.TextField()
    requirement = models.TextField()

    # Comma-separated tags, e.g. "Python, Django, REST"
    tags        = models.CharField(max_length=200, blank=True, default='')

    recruiter   = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='job_posts',
    )

    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Job Post'
        verbose_name_plural = 'Job Posts'

    def __str__(self):
        return f"{self.title} — {self.recruiter.username}"

    @property
    def tag_list(self):
        """Parse the comma-separated tags string into a clean list."""
        if not self.tags:
            return []
        return [t.strip() for t in self.tags.split(',') if t.strip()]


class Application(models.Model):
    """
    Represents a job application submitted by an applicant.

    Each applicant can apply to a job only once (unique_together constraint).
    The uploaded CV is stored under MEDIA_ROOT/cvs/.
    """

    STATUS_CHOICES = (
        ('pending',  'Pending'),
        ('reviewed', 'Reviewed'),
        ('rejected', 'Rejected'),
    )

    job       = models.ForeignKey(
        JobPost,
        on_delete=models.CASCADE,
        related_name='applications',
    )
    applicant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='applications',
    )
    cv_file    = models.FileField(upload_to='cvs/')
    created_at = models.DateTimeField(auto_now_add=True)
    status     = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
    )

    class Meta:
        unique_together = ('job', 'applicant')
        ordering = ['-created_at']
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'

    def __str__(self):
        return f"{self.applicant.username} → {self.job.title} ({self.status})"
