from django.urls import path
from django.contrib.auth.views import  LogoutView
from .views import *


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page='homepage'), name = 'logout'),
    path('register/', RegisterPage.as_view(), name ='register'),
    path('', Homepage.as_view(), name ='homepage'),
    path('booking/', BookingPage.as_view(), name ='booking'),
    path('book/', BookingNoResPage.as_view(), name ='booking_no_resgister'),
    path('service/<int:pk>/', ServiceDetail.as_view(), name='service'),
    path('booking/<int:pk>/', BookingDetail.as_view(), name='booked'),
    
]   
