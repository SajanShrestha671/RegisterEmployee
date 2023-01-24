from django.contrib import admin
from .models import Employee

# Register your models here.
@admin.register(Employee)
class UserAdmin(admin.ModelAdmin):
    list_display: ('firstName','lastName', 'email','image', 'phoneNumber', 'background','position','department','address')