# Generated by Django 3.1.2 on 2021-09-22 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbers_accounts', '0004_auto_20210921_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website_salon_details',
            name='website_logo',
            field=models.ImageField(upload_to=''),
        ),
    ]