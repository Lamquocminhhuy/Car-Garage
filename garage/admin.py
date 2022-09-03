from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Garage)
admin.site.register(Service)
admin.site.register(Booking)
admin.site.register(TimeSlot)

