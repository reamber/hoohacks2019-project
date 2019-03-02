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

    profilePic = models.ImageField(blank=True)

    def __str__(self):
        return self.first_n + ' ' + self.last_n





class Pill(models.Model):
    person = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    pill_text = models.CharField(max_length=500, blank=True)
    startDay = models.DateField(default=datetime.date.today)
    remindTimes = models.TimeField();
    endDay = models.DateField(null=True)

    def __str__(self):
        return self.name
