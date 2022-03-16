"""Admin for the students app."""
from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """Student admin."""
    list_display = (
        'id',
        'first_name',
        'last_name',
        'birthday',
        'enrolled',
        'classes_left',
        'notes'
    )
    search_fields = (
        'first_name',
        'last_name',
        'parent',
        'sales_manager',
        'notes'
    )
