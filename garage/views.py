from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from django.views.generic.edit import CreateView, FormView

from django.views.generic.detail import DetailView
from .models import Garage, Service, Booking
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import login
from .forms import BookingForm, UserCreationForm

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

    
class BookingPage(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'garage/booking.html'
    success_url = reverse_lazy('homepage')