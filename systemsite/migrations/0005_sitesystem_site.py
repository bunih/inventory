# Generated by Django 3.0.7 on 2020-06-18 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('systemsite', '0004_auto_20200618_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesystem',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='systemsite.Place'),
        ),
    ]
