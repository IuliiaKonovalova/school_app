"""Admin for the profiles app."""
from django.contrib import admin
from .models import CustomUser, SalesManager, Teacher, Parent


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    """User admin."""
    list_display = ('id', 'email', 'first_name', 'last_name', 'phone', 'role')
    search_fields = ('phone', 'first_name', 'last_name')


@admin.register(SalesManager)
class SalesManagerAdmin(admin.ModelAdmin):
    """Sales manager admin."""
    list_display = ('id', 'user', 'total_sold')
    search_fields = ('user', 'total_sold')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """Teacher admin."""
    list_display = ('id', 'user',)
    search_fields = ('user',)


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    """Parent admin."""
    list_display = ('id', 'user', 'relation')
    search_fields = ('user', 'relation')
