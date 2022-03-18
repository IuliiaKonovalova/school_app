"""Forms for profiles app"""
from allauth.account.forms import SignupForm
from django import forms
from .models import CustomUser


class SimpleSignupForm(SignupForm):
    """Allauth Signup Form extended"""
    username = forms.CharField(
        max_length=50,
        label='Username',
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    first_name = forms.CharField(
        max_length=30,
        label='First Name',
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=30,
        label='Last Name',
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    phone = forms.CharField(
        max_length=30,
        label='Phone Number',
        widget=forms.TextInput(attrs={'placeholder': 'Phone Number'})
    ) 
    role = forms.IntegerField(widget=forms.HiddenInput(), initial=5)
    def save(self, request):
        print(self.cleaned_data)
        user = super(SimpleSignupForm, self).save(request)
        user.phone = self.cleaned_data.get('phone')
        user.username = self.cleaned_data.get('username')
        user.save()
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.role = self.cleaned_data.get('role')
        user.save()
        return user


class NewApplicationForm(forms.ModelForm):
    """Form for new application"""
    class Meta:
        """Meta class"""
        model = CustomUser
        fields = ['role']
        widgets = {
            'role': forms.Select(attrs={'class': 'form-control'}),
        }


class UserProfileEditForm(forms.ModelForm):
    """Form to edit user profile"""
    class Meta:
        """Meta class"""
        model = CustomUser
        fields = ['first_name', 'last_name', 'phone', 'role']
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'required': True}
            ),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'required': True}
            ),
            'phone': forms.TextInput(
                attrs={'class': 'form-control', 'required': True}
            ),
            'role': forms.Select(
                attrs={
                    'class': 'form-control', 'hidden': True, 'required': False
                }
            ),
        }
