from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django.contrib import admin
import uuid
from django.db import models


# Create your models here.

class Garage(models.Model):
    name = models.CharField(max_length=255, blank=True, verbose_name="Tên cửa hàng")
    description = models.TextField(max_length=2000, blank=True, null=True, verbose_name="Giới thiệu cửa hàng")
    image = models.ImageField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural  = 'Thông Tin Cửa Hàng'


class Service(models.Model):
    name = models.CharField(max_length=255, blank=True, verbose_name='Tên Dịch Vụ')
    price = models.CharField(max_length=255, blank=True , verbose_name='Giá (VND)')
    time_todo = models.CharField(max_length=255, blank=True , verbose_name='Thời gian (phút)')
    description = models.TextField(max_length=255, blank=True, null=True, verbose_name='Mô tả')
    image = models.ImageField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural  = 'Dịch Vụ'


class Booking(models.Model):

    TIMEBLOCK_CHOICES = (
        ("8:00", "8:00"),
        ("9:00", "9:00"),
        ("10:00", "10:00"),
        ("11:00", "11:00"),
        ("01:00", "01:00"), 
        ("02:00", "02:00"),
        ("03:00", "03:00"),
        ("04:00", "04:00"),
        ("05:00", "05:00")
    )
    STATUS_CHOICES = [ 
    ("Đang chờ xử lí", "Đang chờ xử lí"),
    ("Đã xử lí", "Đã xử lí"),
    ("Đã hủy", "Đã hủy"),
    ]

    id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=True, verbose_name="Mã Đơn")
    user = models.CharField(max_length=255, blank=True, null=True, verbose_name="Khách hàng")
    phone_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Số ĐT")
    email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Email")
    date = models.DateField(default=timezone.now,verbose_name="Ngày đặt")
    timeblock = models.CharField(max_length=10, choices=TIMEBLOCK_CHOICES, default="8:00", verbose_name="Thời gian")
    service = models.ForeignKey(Service, on_delete=models.CASCADE,verbose_name= "Dịch vụ")
    note = models.TextField(max_length=300, blank=True, verbose_name="Ghi chú")
    status = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = 'Đang chờ xử lí',
        verbose_name = "Trạng Thái"
        )

    class Meta:
        verbose_name_plural  = 'Lịch hẹn'

    def __str__(self):
        return str(self.user) + " đặt lịch hẹn vào ngày " + str(self.date) + " lúc "+ self.timeblock + " giờ."

    @property
    def get_weekday(self):
        return self.date.strftime("%A")


    




