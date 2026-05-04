from django.contrib import admin
from .models import JobPost


@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display  = ('title', 'recruiter', 'tags', 'created_at')
    list_filter   = ('recruiter',)
    search_fields = ('title', 'tags')
    ordering      = ('-created_at',)
