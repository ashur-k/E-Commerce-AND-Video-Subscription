# Generated by Django 3.1.7 on 2021-03-03 09:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0004_auto_20210225_2204'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscriptions',
            new_name='Subscription',
        ),
        migrations.RenameModel(
            old_name='Videos',
            new_name='Video',
        ),
        migrations.RenameModel(
            old_name='VideosCategory',
            new_name='VideoCategory',
        ),
    ]
