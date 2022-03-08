from django import forms
from .models import *

# create addstudent form
class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'parent', 'birthday', 'classes_bought', 'sales_manager']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'parent': forms.Select(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control'}),
            'classes_have': forms.NumberInput(attrs={'class': 'form-control'}),
            'sales_manager': forms.Select(attrs={'class': 'form-control'}),
        }