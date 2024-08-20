from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='custom_userauths_user_set',
        related_query_name='custom_userauths_user',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_userauths_user_set',
        related_query_name='custom_userauths_user',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
