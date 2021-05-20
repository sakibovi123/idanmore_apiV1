from django import forms
from .models import *
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

