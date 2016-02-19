from django import forms
from todos.models import UserProfile
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = UserProfile
        #fields = ('firstname', 'lastname', 'email', 'password', 'password_confirmation')
        fields = ('user', 'password')