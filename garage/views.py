from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from django.views.generic.edit import CreateView, FormView

from django.views.generic.detail import DetailView
from .models import Garage, Service, Booking, BookingNoRegistration,User
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import login
from .forms import BookingForm, UserCreationForm, BookingNoRegistrationForm
from django.contrib.auth.models import AnonymousUser

from django.contrib import messages


from django.conf import settings
from django.core.mail import send_mail
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

    
class BookingPage(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'garage/booking.html'
    success_url = reverse_lazy('homepage')



    def form_valid(self, form):
        
        form.instance.user = self.request.user

    
        user = User.objects.get(username=self.request.user)
        
        subject = 'Thông báo về lịch hẹn sữa chữa ô tô tại Can Tho Garage'
        message = f"""Cảm ơn quý khách đã đặt lịch với chúng tôi,

Đây là thông tin lịch hẹn của anh/chị:

Tên khách hàng: {user.username}
Ngày đặt: {form.instance.date}
Dịch vụ: {form.instance.service}
Ghi chú: {form.instance.note}

Quý khách vui lòng đến garage vào lúc {form.instance.time_slot} để được hỗ trợ nhanh nhất.
"""
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        send_mail( subject, message, email_from, recipient_list )
   
        return super(BookingPage, self).form_valid(form)

class BookingNoResPage(CreateView):
    model = BookingNoRegistration
    form_class = BookingNoRegistrationForm
    template_name = 'garage/booking_nores.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):    
        subject = 'Thông báo về lịch hẹn sữa chữa ô tô tại Can Tho Garage'
        message = f"""Cảm ơn quý khách đã đặt lịch với chúng tôi,

Đây là thông tin lịch hẹn của anh/chị:

Tên khách hàng: {form.instance.user}
Ngày đặt: {form.instance.date}
Dịch vụ: {form.instance.service}
Ghi chú: {form.instance.note}

Quý khách vui lòng đến garage vào lúc {form.instance.time_slot} để được hỗ trợ nhanh nhất.
"""
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [form.instance.email]
        send_mail( subject, message, email_from, recipient_list )
   
        return super(BookingNoResPage, self).form_valid(form)








