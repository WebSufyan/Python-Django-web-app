from django.db import models
from django.contrib.auth.models import User

from PIL import Image

# Create your models here.
class barber(models.Model):
    barber_name = models.OneToOneField(User, on_delete=models.CASCADE)
    barber_age = models.CharField(max_length=2, blank=True)
    barber_phone = models.CharField(max_length=100, blank=True)
    barber_email = models.EmailField(blank=True)
    barber_pic = models.ImageField(upload_to='media/' , default='', blank=True)
    barber_instagram = models.CharField(max_length=100, blank=True)
    barber_facebook = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.barber_name.username

    # def save(self):
    #     super().save()  # saving image first

    #     img = Image.open(self.barber_pic.path) # Open image using self

    #     if img.height > 420 or img.width > 280:
    #         new_img = (420, 280)
    #         img.resize(new_img)
    #         img.save(self.barber_pic.path)  # saving image at the same path


class barber_gallery(models.Model):
    barber_name = models.ForeignKey(barber, on_delete=models.CASCADE)
    haircut_name = models.CharField(max_length=200, default='', blank=True)
    hairCuts = models.ImageField()

    def __str__(self):
        return self.barber_name.barber_name.first_name

    # def save(self):
    #     super().save()  # saving image first

    #     img = Image.open(self.hairCuts.path) # Open image using self

    #     if img.height > 1600 or img.width > 1000:
    #         new_img = (1600, 1000)
    #         img.thumbnail(new_img)
    #         img.save(self.hairCuts.path)  # saving image at the same path





class website_salon_details(models.Model):
    website_logo = models.ImageField(default='', blank=True)
    website_home_picture = models.ImageField(default='', blank=True)
    # website_salon_address = models.CharField(max_length=300, default='', blank=True)
    # website_hair_service_1 = models.CharField(max_length=300, default='', blank=True)
    # website_hair_service_2 = models.CharField(max_length=300, default='', blank=True)
    # website_hair_service_3 = models.CharField(max_length=300, default='', blank=True)
    # website_hair_service_4 = models.CharField(max_length=300, default='', blank=True)

    def save(self):
        super().save()  # saving image first

        img = Image.open(self.website_logo.path) # Open image using self

        # if img.height > 80 or img.width > 80:
        new_img = (80, 80)
        img = img.resize(new_img)
        img.save(self.website_logo.path)  # saving image at the same path


















