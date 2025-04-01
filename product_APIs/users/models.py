from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    bio = models.TextField(blank=True)
    profile_picture =models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username
