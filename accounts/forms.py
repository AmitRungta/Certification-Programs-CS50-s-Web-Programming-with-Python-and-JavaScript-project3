''' This file is used for creating the custom form for registration '''
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#---------------------------------------------------------------------------
#
class SignupForm(UserCreationForm):
    ''' custom signup form with additional fields '''
    # firstname = forms.CharField(max_length=32, help_text='Required')
    # lastname = forms.CharField(max_length=32, help_text='Required')
    # email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        