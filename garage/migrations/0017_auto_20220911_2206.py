# Generated by Django 3.2 on 2022-09-11 22:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0016_alter_bookingtest_timeblock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingtest',
            name='service',
        ),
        migrations.RemoveField(
            model_name='bookingtest',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='booking',
            options={},
        ),
        migrations.RemoveField(
            model_name='booking',
            name='isCompleted',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='time_slot',
        ),
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Đang chờ xử lí', 'Đang chờ xử lí'), ('Đã xử lí', 'Đã xử lí'), ('Đã hủy', 'Đã hủy')], default='Đang chờ xử lí', max_length=20, verbose_name='Trạng Thái'),
        ),
        migrations.AddField(
            model_name='booking',
            name='timeblock',
            field=models.CharField(choices=[('8:00', '8:00'), ('9:00', '9:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('01:00', '01:00'), ('02:00', '02:00'), ('03:00', '03:00'), ('04:00', '04:00')], default='8:00', max_length=10, verbose_name='Thời gian'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='booking',
            name='note',
            field=models.TextField(blank=True, max_length=300, verbose_name='Ghi chú'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garage.service', verbose_name='Dịch vụ'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Khách hàng'),
        ),
        migrations.DeleteModel(
            name='BookingNoRegistration',
        ),
        migrations.DeleteModel(
            name='BookingTest',
        ),
        migrations.DeleteModel(
            name='TimeSlot',
        ),
    ]
