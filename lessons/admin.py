from django.contrib import admin
from .models import Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """Lesson admin."""
    list_display = ('id', 'date', 'time', 'subject')
    list_filter = ('teachers', 'students')
    search_fields = ('date', 'time', 'subject', 'teachers', 'students')
