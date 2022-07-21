# users/models.py

# import required package for User
from django.contrib.auth.models import AbstractUser
from django.db import models

# create CustomUser class
class CustomUser(AbstractUser):
    pass
