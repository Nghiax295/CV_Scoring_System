from django.db import models
from django.conf import settings


class CV(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cvs'
    )
    file = models.FileField(upload_to='cvs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    extracted_text = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"CV of {self.owner.username} - {self.uploaded_at.strftime('%Y-%m-%d')}"
