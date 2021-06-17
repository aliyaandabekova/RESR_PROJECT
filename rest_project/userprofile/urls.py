from django.urls import path
from .views import *

urlpatterns = [
    path('profile/',ProfileView.as_view(),name='profile'),
    path('register/',RegisterView.as_view(),name='register'),

]