from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_view

from barbers_accounts.views import (register, profile, 
                                    populate_profile, 
                                    update_profile,
                                    modify_account,
                                    password_change,
                                    add_haircuts,
                                    display_gallery,
                                    delete_from_gallery,
                                    client_appointment_update,
                                    client_appointment_delete,
                                    create_website_info,
                                    update_website_info)


urlpatterns = [
    path('register/', register, name='register'),
    path('accounts/profile/', profile, name='profile'),
    path('populate-profile/', populate_profile, name='populate_profile'),
    path('update-profile/', update_profile, name='update_profile'),
    path('account-settings/', modify_account, name='account_settings'),
    path('password-change/', password_change, name='password'),
    path('login/', auth_view.LoginView.as_view(template_name='barbers_accounts/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='barbers_accounts/logout.html'), name='logout'),
    path('adding-haircut/', add_haircuts, name='add_haircut'),
    path('barbers-gallery/', display_gallery, name='barbers_gallery'),
    path('delete-from-gallery/haircut-<int:pk>-delete?', delete_from_gallery, name='delete_haircut_pic'),
    path('client-<int:pk>-updating/', client_appointment_update, name='update_client'),
    path('client-<int:pk>-deleting/', client_appointment_delete, name='delete_client'),
    path('creating-website-info/', create_website_info, name='create_website_info'),
    path('updating-website-info/<int:pk>/', update_website_info, name='update_website_info'),
]




