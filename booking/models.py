from django.db import models

from time import gmtime, strftime

from django.contrib.auth.models import User
# Create your models here.

STATUS_CHOICES = (('ينتظر', 'ينتظر',),
          ('يعمل على قصة شعره', 'يعمل على قصة شعره'),                 
          ('انتهى', 'انتهى'),                 
          ('لم يحضر', 'لم يحضر'))                 


class appointment(models.Model):
    barber_name = models.ForeignKey(User, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=200)
    client_phone_number = models.CharField(max_length=50, default='', blank=True, unique=True, null=True)
    client_desired_hair_cut = models.CharField(max_length=50, default='', blank=True)
    when = models.DateField(default=strftime("%Y-%m-%d", gmtime()))
    appointment_statue = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = 'ينتظر')

    def __str__(self):
        return self.client_name
    
    def save(self, *args, **kwargs):
        if self.client_phone_number != None and self.client_phone_number.strip() == '':
            self.client_phone_number = 'لم يتم إدخال رقم الهاتف'

        super().save(*args, **kwargs) 


# class One_day_booking(models.Model):
#     day = models.ForeignKey(to, on_delete)









