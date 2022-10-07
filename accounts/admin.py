from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'age', 'is_staff']
    
    fieldsets =UserAdmin.fieldsets + (
        (None, {'fields':('age', 'phone_number' )}),
    )

    add_fieldsets =UserAdmin.add_fieldsets + (
        (None, {'fields':('age', 'phone_number' )}),
    )
    
admin.site.register(CustomUser, CustomUserAdmin)
