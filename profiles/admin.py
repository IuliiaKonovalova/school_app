"""Admin for the profiles app."""
from django.contrib import admin
from .models import CustomUser, SalesManager, Parent


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    """User admin."""
    list_display = ('email', 'first_name', 'last_name', 'phone', 'role')
    search_fields = ('phone', 'first_name', 'last_name')


@admin.register(Parent)
class TeacherAdmin(admin.ModelAdmin):
    """Teacher admin."""
    list_display = ('user', 'relation')
    search_fields = ('user', 'relation')


@admin.register(SalesManager)
class SalesManagerAdmin(admin.ModelAdmin):
    """Sales manager admin."""
    list_display = ('user', 'total_sold')
    search_fields = ('user', 'total_sold')
