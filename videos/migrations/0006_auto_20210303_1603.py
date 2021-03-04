# Generated by Django 3.1.7 on 2021-03-03 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_auto_20210303_0923'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'verbose_name_plural': 'Subscriptions'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name_plural': 'UserProfiles'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name_plural': 'Videos'},
        ),
        migrations.AlterModelOptions(
            name='videocategory',
            options={'verbose_name_plural': 'VideoCategories'},
        ),
        migrations.AddField(
            model_name='video',
            name='video_image_thumbnail',
            field=models.ImageField(blank=True, upload_to='video_category_images/image_thumbnails'),
        ),
    ]