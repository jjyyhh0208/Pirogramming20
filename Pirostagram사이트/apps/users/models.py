from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class User(AbstractUser):
    
    name = models.CharField(max_length=24)
    intro = models.TextField(max_length=50, blank = True)
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
    )