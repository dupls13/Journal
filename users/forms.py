# users/forms.py

""" Extends to UserCreation Form and UserChangeForm """

# Import required modules and files
from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from .models import CustomUser

# Create class information

""" Class information for creating Users"""
class CustomUserCreationForm(UserCreationForm):
    # Adds fields required for UserCreation
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields