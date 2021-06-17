from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['profile','product','status','quantity','date_created','total_sum']
    readonly_fields = ['profile','date_created','total_sum']
admin.site.register(Order,OrderAdmin)