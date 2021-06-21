from django.urls import path
from .views import *

urlpatterns = [
    path('category/',CategoryView.as_view(),name='category'),
    path('category/<str:cat_title>/',CategoryProductsView.as_view()),
]