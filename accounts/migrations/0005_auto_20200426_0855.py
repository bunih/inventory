# Generated by Django 3.0.5 on 2020-04-26 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile',
            field=models.ImageField(blank=True, default='images/users/default/brand.png', null=True, upload_to='users/%Y/%m'),
        ),
    ]
