from django.contrib import admin
from .models import *
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['profile','product','text','date_created']
admin.site.register(Comment,CommentAdmin)


class RateAdmin(admin.ModelAdmin):
    list_display = ['profile','product','score']
admin.site.register(Rate,RateAdmin)

