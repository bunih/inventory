# Generated by Django 3.0.7 on 2020-07-21 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systemsite', '0002_remove_sitesystem_guard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesystem',
            name='start_time',
        ),
    ]
