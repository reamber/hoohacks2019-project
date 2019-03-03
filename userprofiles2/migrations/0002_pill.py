# Generated by Django 2.1.7 on 2019-03-03 03:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofiles2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Med1', max_length=200)),
                ('desc', models.CharField(blank=True, max_length=500)),
                ('sDate', models.DateField(default=django.utils.timezone.now)),
                ('time', models.TimeField(default=datetime.time)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
