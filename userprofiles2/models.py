from django.db import models
from django.contrib.auth.models import User
from project import settings
from django.utils.translation import ugettext_lazy as _
import datetime
import django.utils.timezone as timezone


GENDER = (('man', 'Man'), ('woman', 'Woman'))


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, related_name="profile",
                                verbose_name=_('User'), on_delete=models.CASCADE)
    phone = models.PositiveIntegerField(
        null=True, blank=True, verbose_name=_('Phone'))
    gender = models.CharField(
        max_length=40, blank=True, verbose_name=_('Gender'), choices=GENDER)
    avatar = models.ImageField(
        upload_to='userprofiles2/avatars', blank=True, verbose_name=_('Avatar'))
    completion_level = models.PositiveSmallIntegerField(
        default=0, verbose_name=_('Profile completion percentage'))
    email_is_verified = models.BooleanField(
        default=False, verbose_name=_('Email is verified'))
    personal_info_is_completed = models.BooleanField(
        default=False, verbose_name=_('Personal info completed'))

    class Meta:
        verbose_name = _('User profile')
        verbose_name_plural = _('User profiles')

    def __str__(self):
        return "User profile: %s" % self.user.username

    def get_completion_level(self):
        completion_level = 0
        if self.email_is_verified:
            completion_level += 50
        if self.personal_info_is_completed:
            completion_level += 50
        return completion_level

    def update_completion_level(self):
        self.completion_level = self.get_completion_level()
        self.save()


class Pill(models.Model):
    name = models.CharField(max_length=200, default="Med1")
    desc = models.CharField(max_length=500, blank=True)

    sDate = models.DateField(default=timezone.now)
    time = models.TimeField(default=datetime.time)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name="user", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
