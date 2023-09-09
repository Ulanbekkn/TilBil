from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    username = models.CharField(blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='user_media')
    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='custom_users_groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='custom_users_permissions'
    )
