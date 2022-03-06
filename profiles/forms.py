from allauth.account.forms import SignupForm
from django import forms
from matplotlib import widgets
from .models import *

class SimpleSignupForm(SignupForm):
    username = forms.CharField(max_length=30, label='Username')
    first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    phone = forms.CharField(max_length=12, label='Phone Number', widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    role = forms.IntegerField(widget=forms.HiddenInput(), initial=6)
    def save(self, request):
        user = super(SimpleSignupForm, self).save(request)
        user.username = self.cleaned_data.get('username')
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone = self.cleaned_data['phone']
        user.role = self.cleaned_data['role']
        user.save()
        return user


class NewApplicationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['role']
        widgets = {
            'role': forms.Select(attrs={'class': 'form-control'}),
        }
