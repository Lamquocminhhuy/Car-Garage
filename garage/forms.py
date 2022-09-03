from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking     

class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):  

    class Meta:     
        model = Booking
        fields = "__all__"
        widgets = {
            'date': DateInput(),
            'note': forms.Textarea(attrs={'rows': 4})
        }   

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