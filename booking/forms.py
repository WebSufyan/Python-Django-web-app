from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import appointment

from barbers_accounts.models import barber


class DateInput(forms.DateInput):
    input_type = 'date'

class appointment_form(forms.ModelForm):
    class Meta:
        model = appointment
        
        fields = ['barber_name', 'client_name', 'client_phone_number', 'client_desired_hair_cut', 'appointment_statue', 'when']
        
        labels = {'barber_name': 'اختر حلاقك',
                  'client_name': 'اسمك الكامل',
                  'client_phone_number': 'رقم تليفونك',
                  'client_desired_hair_cut': 'قصة الشعر التي تريدها (اختياري)',
                  'when': 'اختر التاريخ',
                  'appointment_statue': 'الحالة (ينتظر ، يعمل على قصة شعره ، انتهى ، لم يحضر)'}
        
        widgets = {'when': DateInput() }


# class signUpForm(UserCreationForm):
#     barber_age = forms.CharField(max_length=2)
#     barber_phone = forms.CharField(max_length=100)
#     barber_email = forms.EmailField()
#     barber_pic = forms.ImageField()
    
#     class Meta:
#         model = User
#         fields = ['username', 'age', 'phone number']


