from django import forms
from todos.models import UserProfile
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    user = forms.CharField(required=True, label='Username')
    firstname = forms.CharField(required=True, label='First Name')
    lastname = forms.CharField(required=True, label='Last Name')
    email = forms.CharField(required=True, label='email')
    password_confirmation = forms.CharField(required=True, widget=forms.PasswordInput())
    
    class Meta:
        model = UserProfile
        fields = ('user','firstname', 'lastname', 'email', 'password', 'password_confirmation')
        
        
        
#class login_form