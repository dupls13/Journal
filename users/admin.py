# users/admin.py
""" Extends CustomUser to AdminUser"""

# install required modules
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# install required files
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

""" Classes """

# Class for Admin
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm 
    list_display = ['email', 'username']
    model = CustomUser
    


admin.site.register(CustomUser, CustomUserAdmin)
