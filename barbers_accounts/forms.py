from django.contrib.auth.models import User
from django import forms

from .models import barber, barber_gallery

from barbers_accounts.models import barber, website_salon_details

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from booking.models import appointment


class userRegisterForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=50) # Required
    last_name = forms.CharField(max_length=50) # Required
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class barber_profile_form(forms.ModelForm):
        
    class Meta:
        model = barber
        
        fields = ['barber_age', 'barber_phone', 'barber_email', 'barber_instagram', 'barber_facebook', 'barber_pic']
        
        labels = {'barber_age': 'عمرك',
                  'barber_phone': 'رقم تليفونك',
                  'barber_email': 'بريدك الإلكتروني',
                  'barber_pic': 'أدخل صورتك (اختياري)',
                  'barber_instagram': 'أدخل رابط الانستقرام الخاص بك (اختياري)',
                  'barber_facebook': 'أدخل رابط ملفك الشخصي على الفيسبوك (اختياري)'}


class barber_gallery_form(forms.ModelForm):

    class Meta:
        model = barber_gallery
        
        fields = ['haircut_name', 'hairCuts']
        
        labels = {'haircut_name': 'اسم قصة الشعر (اختياري)',
                  'hairCuts': 'أدخل قصة الشعر التي قمت بها',}




class account_setting_form(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']



class website_info_form(forms.ModelForm):
    class Meta:
        model = website_salon_details
        fields = '__all__'
        
        labels = {'website_logo': 'شعار الموقع',
                  'website_home_picture': 'صورة الصفحة الرئيسية للموقع',}




