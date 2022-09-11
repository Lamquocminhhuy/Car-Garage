from django.contrib import admin
from .models import *
from django.db import models
# Register your models here.

from django.contrib.auth.models import User
from django.contrib.auth.models import Group


admin.site.unregister(Group)


class Service_Filter(admin.ModelAdmin):
    list_display = ('name', 'price', 'time_todo','description')




class Time_Filter(admin.ModelAdmin):
    list_display = ('time_slot', 'isBusy')

admin.site.register(Garage)
admin.site.register(Service, Service_Filter)
admin.site.register(Booking)

