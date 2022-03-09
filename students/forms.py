"""Forms for students app"""
from django import forms

from profiles.models import Parent
from .models import Student


class AddStudentForm(forms.ModelForm):
    """Form for new student"""
    class Meta:
        """Meta class"""
        model = Student
        fields = [
            'first_name',
            'last_name',
            'parent',
            'parent_relation',
            'birthday',
            'classes_left',
            'sales_manager',
            'notes'
            ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'parent': forms.SelectMultiple(
                attrs={'class': 'form-control'}
                ),
            'birthday': forms.DateInput(attrs={'class': 'form-control'}),
            'classes_left': forms.NumberInput(attrs={'class': 'form-control'}),
            'sales_manager': forms.SelectMultiple(
                attrs={'class': 'form-control'}
                ),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
            'parent_relation': forms.Select(
                attrs={'class': 'form-control'},
                choices=Parent.GUARDIAN_RELATION
            )
        }
