# add form to sales/forms.py which takes in the sales model and returns a form with fields
from django import forms
from .models import Sales


class SalesForm(forms.ModelForm):
    """Form for sales"""
    class Meta:
        model = Sales
        fields = ['sold_by', 'sold_to', 'amount', 'date']
        widgets = {
            'sold_by': forms.Select(attrs={'class': 'form-control'}),
            'sold_to': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'})
        }