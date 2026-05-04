from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display  = ('username', 'email', 'role', 'is_staff', 'is_superuser')
    list_filter   = ('role', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')

    # Add 'role' to the user detail page under a new section
    fieldsets = UserAdmin.fieldsets + (
        ('Role', {'fields': ('role',)}),
    )
