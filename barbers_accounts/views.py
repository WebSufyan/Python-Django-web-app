from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

import os

from .forms import (barber_profile_form, 
                    userRegisterForm, 
                    barber_gallery_form, 
                    account_setting_form,
                    website_info_form)

from django.contrib.auth.models import User
from .models import barber, barber_gallery, website_salon_details


from booking.forms import appointment_form
from booking.models import appointment




# Create your views here.
def register(request):
    if request.method == 'POST':
        form = userRegisterForm(request.POST)
        if form.is_valid():

            form.save()
            usrname = form.cleaned_data.get('username')
            messages.success(request, f'تم إنشاء الحساب لـ {usrname}!')
            return redirect('login')
    else:
        form = userRegisterForm()

    return render(request, 'barbers_accounts/register.html', {'form': form})




@login_required
def profile(request):
    return render(request, 'barbers_accounts/profile.html')




@login_required
def populate_profile(request):
    if request.method == 'POST':
        form = barber_profile_form(request.POST)
        if form.is_valid():
            
            form.instance.barber_name = request.user
            form.save()
            messages.success(request, 'تم إنشاء ملف التعريف الخاص بك!')
            
            return redirect('profile')
    else:
        form = barber_profile_form()
    
    return render(request, 'barbers_accounts/populate_profile.html', {'form': form})




@login_required
def update_profile(request):
    if request.method == 'POST':
        form = barber_profile_form(request.POST, request.FILES, instance=request.user.barber)
        if request.user.barber.barber_pic:
            if os.path.isfile(request.user.barber.barber_pic.path):
                os.remove(request.user.barber.barber_pic.path)

        if form.is_valid():

            form.instance.barber_name = request.user
            form.save()
            messages.success(request, 'تم تحديث الملف الشخصي!')

            return redirect('profile')
    else:
        form = barber_profile_form(instance=request.user.barber)
    
    return render(request, 'barbers_accounts/update_profile.html', {'form': form})




@login_required
def modify_account(request):
    if request.method == 'POST':
        name_form = account_setting_form(request.POST, request.FILES, instance = request.user)
        if name_form.is_valid():
            name_form.save()
            messages.success(request, 'تم تعديل الأسماء في الحساب!')

            return redirect('profile')
    else:
        name_form = account_setting_form(instance = request.user)

    context = {'name_form': name_form}
    
    return render(request, 'barbers_accounts/account_settings.html', context)




@login_required
def password_change(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'تم تغيير كلمة المرور!')

            return redirect('profile')
    else:
        password_form = PasswordChangeForm(request.user)

    context = {'password_form': password_form}
    
    return render(request, 'barbers_accounts/password.html', context)




@login_required
def add_haircuts(request):
    if request.method == 'POST':
        haircut_form = barber_gallery_form(request.POST, request.FILES)
        if haircut_form.is_valid():
            
            haircut_form.instance.barber_name = request.user.barber
            haircut_form.save()
            messages.success(request, 'تمت إضافة صورة قصة شعر!')

            return redirect('add_haircut')
    else:
        haircut_form = barber_gallery_form()

    context = {'haircut_form': haircut_form}
    
    return render(request, 'barbers_accounts/add_haircut_forBarber.html', context)




@login_required
def display_gallery(request):

    barbers_gallery = barber_gallery.objects.filter(barber_name=request.user.barber)
    context = {'barbers_gallery': barbers_gallery}
    
    return render(request, 'barbers_accounts/haircuts_gallery.html', context)




@login_required
def delete_from_gallery(request, pk):

    pic_from_gallery = barber_gallery.objects.get(id=pk)
    if request.method == 'POST':

        if pic_from_gallery.hairCuts:
            os.remove(pic_from_gallery.hairCuts.path)

        pic_from_gallery.delete()
        messages.success(request, 'تم حذف صورة قصة الشعر!')

        return redirect('barbers_gallery')

    return render(request, 'barbers_accounts/haircuts_gallery.html')




@login_required
def client_appointment_update(request, pk):
    
    appoints = appointment.objects.get(id=pk)

    if request.method == 'POST':
        form = appointment_form(request.POST, instance=appoints)

        if form.is_valid():
            form.save()
            form = appointment_form(request.POST, instance=appoints)
            messages.success(request, 'تم تحديث العميل')
            return redirect('appointments_list')
    else:
        form = appointment_form(instance=appoints)
    
    return render(request, 'booking/update_client.html', {'form': form})




@login_required
def client_appointment_delete(request, pk):
    
    appoints = appointment.objects.get(id=pk)

    if request.method == 'POST':
        appoints.delete()
        messages.success(request, 'تم حذف العميل نهائيا')
        return redirect('appointments_list')
    
    return render(request, 'booking/list_bookings.html')



@login_required
def create_website_info(request):

    if request.method == 'POST':
        form = website_info_form(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            form = website_info_form(request.POST)
            messages.success(request, 'تم إنشاء معلومات الموقع')
            return redirect('home')
    else:
        form = website_info_form()
    
    return render(request, 'barbers_accounts/create_website_info.html', {'form': form})




@login_required
def update_website_info(request, pk):

    website_info = website_salon_details.objects.get(pk = pk)
    if request.method == 'POST':
        form = website_info_form(request.POST, request.FILES, instance=website_info)
        if website_info.website_logo and website_info.website_home_picture:
            if os.path.isfile(website_info.website_logo.path) and os.path.isfile(website_info.website_home_picture.path):
                os.remove(website_info.website_logo.path)
                os.remove(website_info.website_home_picture.path)
            
        if form.is_valid():  
            form.save()
            form = website_info_form(request.POST, instance=website_info)
            messages.success(request, 'تم تحديث معلومات الموقع')
            return redirect('home')
    else:
        form = website_info_form(instance=website_info)
    
    return render(request, 'barbers_accounts/create_website_info.html', {'form': form})







