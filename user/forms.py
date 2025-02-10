from typing import Any
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
import datetime


def validate_birthday(value):
    if value > datetime.date.today():
        raise ValidationError("تاریخ تولد نمی‌تواند در آینده باشد!")
    


class UserRegisterForm(UserCreationForm):
    birthday=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date'}),validators=[validate_birthday])
    
    class Meta:
        model=User
        fields=['email','first_name','last_name','birthday','password1','password2']

    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'نام'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'نام خانوادگی'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'رمز عبور'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'تأیید رمز عبور'})

