# from allauth.account.forms import SignupForm
from django import forms
from .models import *


# need to add extra fields to standard allauth SignupForm
class NewSignupForm(forms.Form):
    # role = forms.ChoiceField(choices=ROLES, widget=forms.RadioSelect)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone_number = forms.CharField(max_length=30, required=True)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone_number = self.cleaned_data['phone_number']
        user.save()
        return user
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_number', 'role', 'email', 'password1', 'password2')
