from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
