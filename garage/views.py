from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from django.views.generic.edit import CreateView, FormView

from django.views.generic.detail import DetailView
from .models import *
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import login
from .forms import *
from django.contrib.auth.models import AnonymousUser

from django.contrib import messages


from django.conf import settings
from django.core.mail import send_mail
import datetime
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'garage/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('homepage')

class RegisterPage(FormView):
    template_name = 'garage/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('homepage')
        return super(RegisterPage, self).get(*args, **kwargs)

class Homepage(ListView):
    model = Service
    template_name = 'garage/index.html'
    context_object_name = 'services'   

    def get_context_data(self, **kwargs):
        context = super(Homepage, self).get_context_data(**kwargs)
        context['garage'] = Garage.objects.get(id=1)
        return context

class ServiceDetail(DetailView):
    model = Service
    context_object_name = 'service'

    

def generate_daylist():
    daylist = []
    today = datetime.date.today()
    map = {
    "MONDAY": "THỨ HAI",
    "TUESDAY": "THỨ BA",
    "WEDNESDAY": "THỨ TƯ",
    "THURSDAY": "THỨ NĂM",
    "FRIDAY": "THỨ SÁU",
    "SATURDAY": "THỨ BẢY",
    "SUNDAY": "CHỦ NHẬT"
    }
    for i in range(7):
        day = {}
        curr_day = today + datetime.timedelta(days=i)
        weekday = curr_day.strftime("%A").upper()

        day["date"] = str(curr_day)
        day['day'] = map[weekday]

        day["A_booked"] = (
            Booking.objects.filter(date=str(curr_day)).filter(timeblock="8:00").exists()
        )
        day["B_booked"] = (
            Booking.objects.filter(date=str(curr_day)).filter(timeblock="9:00").exists()
        )
        day["C_booked"] = (
            Booking.objects.filter(date=str(curr_day)).filter(timeblock="10:00").exists()
        )
        day["D_booked"] = (
            Booking.objects.filter(date=str(curr_day)).filter(timeblock="11:00").exists()
        )
        day["E_booked"] = (
            Booking.objects.filter(date=str(curr_day)).filter(timeblock="01:00").exists()
        )
        day["F_booked"] = (
            Booking.objects.filter(date=str(curr_day)).filter(timeblock="02:00").exists()
        )
        day["G_booked"] = (
            Booking.objects.filter(date=str(curr_day)).filter(timeblock="03:00").exists()
        )
        day["H_booked"] = (
            Booking.objects.filter(date=str(curr_day)).filter(timeblock="04:00").exists()
        )
        day["I_booked"] = (
            Booking.objects.filter(date=str(curr_day)).filter(timeblock="05:00").exists()
        )
        if day["day"] != "SATURDAY":  # Writing lab doesn't open on Saturday
            daylist.append(day)
    return daylist


def booking(request):
    services = Service.objects.all()
    context = {"days": generate_daylist(), "services": services}
   
    return render(request, "garage/booking.html", context)



def BookingPage(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        date = request.POST.get("date")
        time = request.POST.get("time")
        service = request.POST.get("service")
        note = request.POST.get("note")

        service_b = Service.objects.get(id=service)
       
        booking = Booking(user = name, email = email, date= date, timeblock= time, service= service_b, note= note)
        booking.save()


   
        # Send email
        if email:
            subject = 'Thông báo về lịch hẹn sữa chữa ô tô tại Can Tho Garage'
            message = f"""Cảm ơn quý khách đã đặt lịch với chúng tôi,
Đây là thông tin lịch hẹn của anh/chị:
Tên khách hàng: {name}
Ngày đặt: {date}
Dịch vụ: {service_b}
Ghi chú: {note}
Quý khách vui lòng đến garage vào lúc {time} để được hỗ trợ nhanh nhất.
"""
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )



    return HttpResponse("hshshs")
