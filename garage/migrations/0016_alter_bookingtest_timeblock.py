# Generated by Django 3.2 on 2022-09-11 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0015_bookingtest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingtest',
            name='timeblock',
            field=models.CharField(choices=[('8:00', '8:00'), ('9:00', '9:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('01:00', '01:00'), ('02:00', '02:00'), ('03:00', '03:00'), ('04:00', '04:00')], default='8:00', max_length=10),
        ),
    ]
