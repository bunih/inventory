# Generated by Django 3.0.7 on 2020-06-18 16:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('systemsite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesystem',
            name='guard',
        ),
        migrations.AddField(
            model_name='sitesystem',
            name='guard',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]