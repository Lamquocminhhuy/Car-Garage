from django.urls import path
from django.contrib.auth.views import  LogoutView
from .views import *

# fill data
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page='homepage'), name = 'logout'),
    path('register/', RegisterPage.as_view(), name ='register'),
    path('', Homepage.as_view(), name ='homepage'),

    path('service/<int:pk>/', ServiceDetail.as_view(), name='service'),

    path("booking/", booking, name="booking"),
    path("booking_test/", BookingPage, name="booking_test"),
    
]   
