from django.shortcuts import render, redirect
from booking.models import appointment
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.models import User

from barbers_accounts.models import barber
from barbers_accounts.models import barber_gallery, website_salon_details

from .forms import appointment_form

from django.contrib import messages

from time import gmtime, strftime

# Create your views here.

def home(request):
    
    # if website_salon_details.objects.all():
    #     salon_details = website_salon_details.objects.get(pk=1)
    #     salon_logo = salon_details.website_logo
    #     salon_picture = salon_details.website_home_picture
        
    #     context = {'salon_logo': salon_logo,
    #                'salon_picture': salon_picture}
        
    #     return render(request, 'booking/home.html', context)
    # else:
    return render(request, 'booking/home.html')




# list all available barbers
class ListBarbers(ListView):

    model = barber

    template_name = 'booking/list_barbers.html'




class barberDetail(DetailView):
    
    context_object_name = 'barber'
    template_name = 'booking/barber_detail.html'
    
    

def display_gallery(request, pk):

    barbers_gallery = barber_gallery.objects.filter(barber_name=pk)
    
    if len(barbers_gallery) > 0:
        barber_name = barbers_gallery[0].barber_name.barber_name.username
        context = {'barbers_gallery': barbers_gallery,
               'barber_name': barber_name}
    else:
        context = {'barbers_gallery': barbers_gallery}
    
    # context = {'barbers_gallery': barbers_gallery,
    #            'barber_name': barber_name}
    
    return render(request, 'booking/barbers_gallery.html', context)




# booking the appointment
def book(request):

    if request.method == 'POST':
        form = appointment_form(request.POST)

        if form.is_valid():
            form.save()
            form = appointment_form()
            messages.success(request, 'لقد تم وضعك في قائمة الانتظار')
            return redirect('barbers_booking_list')
    else:
        form = appointment_form()


    return render(request, 'booking/book.html', {'form': form})




def list_appointments(request, pk):
    appointments = appointment.objects.filter(when=strftime("%Y-%m-%d", gmtime())).filter(barber_name=pk)
    current_user = User.objects.get(pk = pk)

    numbers_of_appointments_today = []
    appointments_numbers = 0
    
    for entry in appointments:
        appointments_numbers += 1
        numbers_of_appointments_today.append(appointments_numbers)

    appointments_and_numbers = zip(appointments, numbers_of_appointments_today)

    context = {'appointments_and_numbers': appointments_and_numbers,
               'current_user': current_user}

    return render(request, 'booking/list_bookings.html', context)



class ListBarbers_for_bookings(ListView):

    model = User

    template_name = 'booking/list_barbers_for_booking.html'



























    
