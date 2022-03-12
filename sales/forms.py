from django import forms
from .models import Sales
from students.models import Student


class SalesForm(forms.ModelForm):

    student = forms.ModelChoiceField(queryset=Student.objects.all())
    class Meta:
        model = Sales
        fields = ['sold_to', 'amount'] + ['student']
        widgets = {
            'sold_to': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }
