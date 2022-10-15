from functools import partial
from urllib import response

from garage.utils.daylist import generate_daylist
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login

from django.urls import reverse_lazy
from django.conf import settings
from django.core.mail import send_mail

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import BookingSerializer, UserSerializer, GroupSerializer, ServiceSerializer

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.http import Http404

@api_view(['POST'])
def update_booking(request,booking_id):

    """
    Update booking
    """

    booking = Booking.objects.get(id__startswith=booking_id)
    serializer = BookingSerializer(instance=booking, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

@api_view(['GET'])
def get_booking(request,booking_id):
    """
    Get booking information
    """
    if request.method == 'GET':
        booking = Booking.objects.get(id__startswith=booking_id)
        serializer = BookingSerializer(booking)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


@api_view(['POST'])
@csrf_exempt
def create_booking(request):
    """
    Create a new booking
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookingSerializer(data=data)
        print(data)
        service = Service.objects.get(id=data['service'])
        if serializer.is_valid():
            serializer.save()
#             subject = 'Thông báo về lịch hẹn sữa chữa ô tô tại Can Tho Garage'
#             message = f"""Cảm ơn quý khách đã đặt lịch với chúng tôi,
#     Đây là thông tin lịch hẹn của anh/chị: 
#     Mã đơn: {data.id.hex[0:8]}
#     Tên khách hàng: {data.user}
#     Số ĐT liên lạc: {data.phone_number}
#     Ngày đặt: {data.date}
#     Dịch vụ: {service.name}
# Quý khách vui lòng đến garage vào lúc {data.time} để được hỗ trợ nhanh nhất.

# Nếu có thắc mắc hoặc yêu cầu hỗ trợ quý khách có thể liên lạc với chúng tôi qua sđt 0123456789.
# """
#             email_from = settings.EMAIL_HOST_USER
#             recipient_list = [data.email]
#             send_mail( subject, message, email_from, recipient_list )
            return JsonResponse(serializer.data, status=201, json_dumps_params={'ensure_ascii': False})
        return JsonResponse(serializer.errors, status=400, json_dumps_params={'ensure_ascii': False})

@api_view(['GET'])
@csrf_exempt
def service_list(request):
    """
    Get all list of services
    """
    if request.method == 'GET':
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

@api_view(['GET'])
@csrf_exempt
def service_detail(request,name):
    """
    Get specific service detail by name
    """
    try:
    
        service = Service.objects.get(name__contains=name.capitalize())
       
    except Service.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        serializer = ServiceSerializer(service)
        return JsonResponse(serializer.data, json_dumps_params={'ensure_ascii': False})

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



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

    

def booking(request):
    services = Service.objects.all()
    context = {"days": generate_daylist(), "services": services}
   
    return render(request, "garage/booking.html", context)



def BookingPage(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        date = request.POST.get("date")
        time = request.POST.get("time")
        service = request.POST.get("service")
        note = request.POST.get("note")

        service_b = Service.objects.get(id=service)
       
        booking = Booking(user = name, email = email, date= date, timeblock= time, service= service_b, note= note, phone_number=phone_number)
   
        booking.save()

        # Send email
        if email:
            subject = 'Thông báo về lịch hẹn sữa chữa ô tô tại Can Tho Garage'
            message = f"""Cảm ơn quý khách đã đặt lịch với chúng tôi,
    Đây là thông tin lịch hẹn của anh/chị: 
    Mã đơn: {booking.id.hex[0:8]}
    Tên khách hàng: {name}
    Số ĐT liên lạc: {phone_number}
    Ngày đặt: {date}
    Dịch vụ: {service_b}
Quý khách vui lòng đến garage vào lúc {time} để được hỗ trợ nhanh nhất.

Nếu có thắc mắc hoặc yêu cầu hỗ trợ quý khách có thể liên lạc với chúng tôi qua sđt 0123456789.
"""
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )



    return HttpResponse("Worked")
