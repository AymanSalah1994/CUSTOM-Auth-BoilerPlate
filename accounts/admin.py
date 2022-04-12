from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.
class CustomUserAdmin(UserAdmin):
    # Form To add a New User
    add_form = CustomUserCreationForm
    

    # Form To Edit A User
    form = CustomUserChangeForm
    

    # Model To Edit/instaciate From 
    model = CustomUser


    # Fields To Show In The Admin Page
    list_display = ['email', 'username', 'mobileNumber', 'city', 'is_staff']

    # Fields to be used in editing users
    filedsets = UserAdmin.fieldsets + (None , {'fields': ('mobileNumber',)})

# Fields To Show In The Admin Page
admin.site.register(CustomUser, CustomUserAdmin)