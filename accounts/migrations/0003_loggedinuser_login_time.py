# Generated by Django 2.2 on 2019-04-14 15:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_loggedinuser_login_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='loggedinuser',
            name='login_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
