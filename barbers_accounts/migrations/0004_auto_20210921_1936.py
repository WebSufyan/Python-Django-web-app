# Generated by Django 3.1.2 on 2021-09-21 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbers_accounts', '0003_auto_20210919_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='website_salon_details',
            name='website_hair_service_1',
        ),
        migrations.RemoveField(
            model_name='website_salon_details',
            name='website_hair_service_2',
        ),
        migrations.RemoveField(
            model_name='website_salon_details',
            name='website_hair_service_3',
        ),
        migrations.RemoveField(
            model_name='website_salon_details',
            name='website_hair_service_4',
        ),
        migrations.RemoveField(
            model_name='website_salon_details',
            name='website_salon_address',
        ),
        migrations.AlterField(
            model_name='website_salon_details',
            name='website_home_picture',
            field=models.ImageField(upload_to=''),
        ),
    ]