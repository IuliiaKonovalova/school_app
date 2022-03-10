from django import forms
from .models import Sales


class SalesForm(forms.Form):
    classes_bought = forms.IntegerField(label='Classes bought', min_value=1, max_value=100)
    """Form for sales"""
    class Meta:
        model = Sales

    def save(self, request):
        """Save form"""
        sales = super(SalesForm, self).save(commit=False)
        sales.sold_by = request.user
        sales.sold_to = request.user.parent
        sales.classes_bought = self.cleaned_data.get('classes_bought')
