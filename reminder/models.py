from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class Person(models.Model):
    first_n = models.CharField(max_length=200)
    last_n = models.CharField(max_length=200)
    email = models.EmailField()

    profilePic = models.ImageField()

    def __str__(self):
        return self.first_n + ' ' + self.last_n


class Pill(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    pill_text = models.CharField(max_length=500)
    startDay = models.DateField(default=datetime.date.today)
    remindTimes = models.TimeField();
    endDay = models.DateField(null=True)

    def __str__(self):
        return self.name
