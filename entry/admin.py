# entry/admin.py
from django.contrib import admin

from . import models 

#Adds Entry to admin contorls 
admin.site.register(models.Entry)