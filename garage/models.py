from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Garage(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(max_length=2000, blank=True, null=True)
    image = models.ImageField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TimeSlot(models.Model):
    isBusy = models.BooleanField(default=False)
    time_slot = models.CharField(max_length=255, blank=True, null=True)
    

    def __str__(self):
        return self.time_slot

class Service(models.Model):
    name = models.CharField(max_length=255, blank=True)
    price = models.CharField(max_length=255, blank=True)
    time_todo = models.CharField(max_length=255, blank=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    image = models.ImageField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    note = models.TextField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        return str(self.user) + " đặt lịch vào " + str(self.time_slot) + " ngày " + str(self.date)




