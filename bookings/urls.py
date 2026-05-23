from django.urls import path
from . import views

urlpatterns=[
    path('create/<int:restaurant_id>/',views.booking_create,name='booking_create'),
    path('',views.booking_list,name='booking_list'),
    path('cancel/<int:pk>/',views.booking_cancel,name='booking_cancel'),

]