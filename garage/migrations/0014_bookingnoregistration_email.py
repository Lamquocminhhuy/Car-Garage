# Generated by Django 3.2.15 on 2022-09-10 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0013_alter_booking_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingnoregistration',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email'),
        ),
    ]