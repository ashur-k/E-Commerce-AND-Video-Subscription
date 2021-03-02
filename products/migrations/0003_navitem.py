# Generated by Django 3.1.7 on 2021-02-23 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210223_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Nav-Items',
            },
        ),
    ]