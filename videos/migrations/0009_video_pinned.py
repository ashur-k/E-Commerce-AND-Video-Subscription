# Generated by Django 3.1.7 on 2021-03-11 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_video_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
    ]