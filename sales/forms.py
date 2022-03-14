"""Forms for the sales app."""
from django import forms
from students.models import Student
from .models import Sales


class SalesForm(forms.ModelForm):
    """Sales form"""
    student = forms.ModelChoiceField(queryset=Student.objects.all())
    class Meta:
        """Meta class"""
        model = Sales
        fields = ['sold_to', 'amount'] + ['student']
        widgets = {
            'sold_to': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }
