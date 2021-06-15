from django.contrib import admin
from .models import *

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','full_name','email','address','wallet','photo','order_count','sale']
admin.site.register(Profile,ProfileAdmin)

