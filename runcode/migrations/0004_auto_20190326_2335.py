# Generated by Django 2.1.7 on 2019-03-26 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runcode', '0003_auto_20190325_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='pycode',
            name='session',
            field=models.TextField(default='null', max_length=40),
        ),
        migrations.AddField(
            model_name='uservids',
            name='session',
            field=models.TextField(default='null', max_length=40),
        ),
    ]
