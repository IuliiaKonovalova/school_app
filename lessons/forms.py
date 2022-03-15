"""Forms for the lessons app."""
from django import forms
from .models import Lesson


class LessonForm(forms.ModelForm):
    """Lesson form."""
    class Meta:
        """Meta class."""
        model = Lesson
        fields = ['date', 'time_period', 'subject', 'teachers', 'students']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'time_period': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'teachers': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'students': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }