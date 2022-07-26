"""journal_project URL Configuration"""
# journal_project/urls.py
""" Connect urls to user app """
from django.contrib import admin
from django.urls import path, include 
from django.views.generic.base import TemplateView

urlpatterns = [
    path('entry/', include('entry.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
]
