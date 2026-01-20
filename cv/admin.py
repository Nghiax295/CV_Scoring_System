from django.contrib import admin
from .models import CV


@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ('owner', 'file', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('owner__username',)
    readonly_fields = ('uploaded_at',)
