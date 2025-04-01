from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    # a custom backend is being used for username/email/phone number login
    # but the USERNAME_FIELD here is for choosing the default one in case more than email is provided
    # also it makes it so that email is now required for registration 
    USERNAME_FIELD = 'email'
    # to avoid errors REQUIRED_FIELDS must be set even if it is an empty list but here we require a username as well
    # tried looking it up but couldn't find the solution for now
    REQUIRED_FIELDS = ['username']
    bio = models.TextField(blank=True)
    profile_picture =models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username
