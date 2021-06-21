from django.urls import path
from .views import *

urlpatterns = [
    path('order/',OrderPostView.as_view(),name='order'),
    path('my_orders/',MyOrderView.as_view()),
    path('modify_order/<int:order_id>/',UpdateDeleteView.as_view(),name='modify_order'),

]