# Generated by Django 3.1.7 on 2021-02-25 21:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VideosCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_category', models.CharField(max_length=254)),
                ('image', models.ImageField(upload_to='video_category_images/')),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
                ('slug_Field', models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(max_length=30)),
                ('video_description', models.CharField(max_length=255)),
                ('video_URL', models.URLField(max_length=300)),
                ('can_view', models.BooleanField(default=False)),
                ('video_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='videos.videoscategory')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.ImageField(upload_to='user_images/')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('address_line_1', models.CharField(blank=True, max_length=80, null=True)),
                ('address_line_2', models.CharField(blank=True, max_length=80, null=True)),
                ('county_town_or_city', models.CharField(blank=True, max_length=80, null=True)),
                ('postal_or_zip_code', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_subscription', models.BooleanField(default=False)),
                ('subscription_start_date', models.DateField(blank=True, null=True)),
                ('subscription_expiry_date', models.DateField(blank=True, null=True)),
                ('subscription_type', models.CharField(choices=[('F', 'FREE'), ('M', 'MONTHLY'), ('Y', 'YEARLY')], default='FREE', max_length=100)),
                ('subscription_price', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
