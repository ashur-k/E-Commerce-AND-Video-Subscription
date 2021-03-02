# Generated by Django 3.1.7 on 2021-02-23 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_navitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NavItem',
        ),
        migrations.AlterField(
            model_name='category',
            name='parent_name',
            field=models.CharField(choices=[('clothing', 'clothing'), ('homeware', 'homeware'), ('discount-offers', 'discount-offers'), ('new-arrivals', 'new-arrivals')], max_length=25),
        ),
    ]