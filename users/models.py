from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone
import datetime
# Create your models here.

class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    objects = CustomUserManager()
    first_n = models.CharField(max_length=200, blank=True)
    last_n = models.CharField(max_length=200, blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.first_n + ' ' + self.last_n


