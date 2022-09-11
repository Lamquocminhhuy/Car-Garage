# Generated by Django 3.2 on 2022-09-11 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('garage', '0014_bookingnoregistration_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('timeblock', models.CharField(choices=[('A', '8:00'), ('B', '9:00'), ('C', '10:00'), ('D', '11:00'), ('E', '01:00'), ('F', '02:00'), ('G', '03:00'), ('H', '04:00')], default='A', max_length=10)),
                ('note', models.TextField(blank=True, max_length=300)),
                ('status', models.CharField(choices=[('Đang chờ xử lí', 'Đang chờ xử lí'), ('Đã xử lí', 'Đã xử lí'), ('Đã hủy', 'Đã hủy')], default='Đang chờ xử lí', max_length=20, verbose_name='Trạng Thái')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garage.service', verbose_name='Dịch vụu')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Khách hàng')),
            ],
        ),
    ]