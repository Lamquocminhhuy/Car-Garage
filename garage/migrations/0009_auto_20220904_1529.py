# Generated by Django 3.2.15 on 2022-09-04 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0008_auto_20220904_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workingdate',
            name='time_slot',
        ),
        migrations.AddField(
            model_name='workingdate',
            name='time_slot',
            field=models.ManyToManyField(to='garage.TimeSlot'),
        ),
    ]
