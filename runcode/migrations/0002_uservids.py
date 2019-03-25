# Generated by Django 2.1.7 on 2019-03-25 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('runcode', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postdate', models.DateTimeField(verbose_name='time saved')),
                ('uservid', models.FilePathField(path='runcode/data/videos')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
