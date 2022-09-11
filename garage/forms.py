from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'





class UserCreationForm(UserCreationForm):

    email = forms.EmailField(required=True, label='Email')
    password1 = forms.CharField(
        label='Mật khẩu',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
  
    )
    password2 = forms.CharField(
        label='Xác nhận',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
     
    )


    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        labels  = {
            "username": "Tên đăng nhập",
            "email": "Email",
        }

      

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


  

