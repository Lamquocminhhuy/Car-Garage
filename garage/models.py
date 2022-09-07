from django.db import models
from django.contrib.auth.models import User

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

class TimeSlot(models.Model):
    isBusy = models.BooleanField(default=False, verbose_name="Nghỉ")
    time_slot = models.CharField(max_length=255, blank=True, null=True, verbose_name="Khung giờ")
    

    def __str__(self):
        return self.time_slot
    class Meta:
        verbose_name_plural  = 'Thời gian làm việc'

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
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Khách hàng")
    
    service = models.ForeignKey(Service, on_delete=models.CASCADE,verbose_name= "Dịch vụ")
    date = models.DateField(null=True, verbose_name="Ngày đặt")
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, verbose_name="Khung giờ")
    note = models.TextField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Số ĐT")
    isCompleted = models.BooleanField(default=False, verbose_name="Đã xử lí")


    def __str__(self):
        return str(self.user) + " đặt lịch vào " + str(self.time_slot) + " ngày " + str(self.date)
    
    class Meta:
        verbose_name_plural  = 'Lịch hẹn'

class BookingNoRegistration(models.Model):
    user = models.CharField(max_length=255, blank=True, null=True,verbose_name="Khách hàng")
    service = models.ForeignKey(Service, on_delete=models.CASCADE,verbose_name= "Dịch vụ")
    date = models.DateField(null=True, verbose_name="Ngày đặt")
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, verbose_name="Khung giờ")
    note = models.TextField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Số ĐT")
    isCompleted = models.BooleanField(default=False, verbose_name="Đã xử lí")


    def __str__(self):
        return self.user + " đặt lịch vào " + str(self.time_slot) + " ngày " + str(self.date)
    
    class Meta:
        verbose_name_plural  = 'Lịch hẹn (khách vãng lai)'



