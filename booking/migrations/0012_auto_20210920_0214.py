# Generated by Django 3.1.2 on 2021-09-20 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_auto_20210920_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_statue',
            field=models.CharField(choices=[('waiting', 'ينتظر'), ('in progress', 'يعمل على قصة شعره'), ('finished', 'انتهى'), ('did not show up', 'لم يحضر')], default=('waiting', 'ينتظر'), max_length=20),
        ),
    ]