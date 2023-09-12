from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, User


class User1(AbstractUser):
    email = models.EmailField(unique=True)

    class Meta:
        swappable = 'AUTH_USER_MODEL'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


User1.groups.related_name = 'custom_user_set'
User1.user_permissions.related_name = 'custom_user_set'
