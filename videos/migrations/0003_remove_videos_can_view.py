# Generated by Django 3.1.7 on 2021-02-25 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_videos_is_free_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videos',
            name='can_view',
        ),
    ]