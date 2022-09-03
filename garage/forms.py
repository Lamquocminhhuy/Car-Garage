from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking, TimeSlot

class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):  

    class Meta:     
        model = Booking
        fields = ["service", "date", "time_slot", "phone_number", "note"]
        widgets = {
            'date': DateInput(),
            'note': forms.Textarea(attrs={'rows': 4})
        }   
        labels  = {
            "service": "Dịch vụ",
            "date": "Ngày đặt lịch",
            "time_slot": "Thời gian",
            "note": "Ghi chú",
            "phone_number": "Số điện thoại"

        }
    def __init__(self, user=None, **kwargs):
        super(BookingForm, self).__init__(**kwargs)
        self.fields['time_slot'].queryset = TimeSlot.objects.filter(isBusy=False)

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
      

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user