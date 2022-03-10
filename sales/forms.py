from django import forms


class SalesForm(forms.Form):
    classes_sold = forms.IntegerField(label='Classes sold', min_value=1, max_value=100)
    sold_to = forms.Select()
    sold_to_child = forms.Select()
