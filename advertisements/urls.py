from django.contrib import admin
from django.urls import path,include
from .views import *


app_name = "advert"

urlpatterns=[
    path('add_room/<int:id>',house_detail,name="house_detail"),
    path('room_detail/<int:pk>',RoomDetail.as_view(), name="room_detail"),
    path('room/delete/<int:pk>/',delete_room , name="delete"),
    path('accounts/profile/<int:pk>', profile_view, name='profile'),
    path('profile_update/',edit_profile , name="edit_profile"),
    path('house_update/<int:pk>' , house_update , name="update_house"),
    path('house_delete/<int:pk>',delete_house,name="delete_house"),
    path('update_room/<int:pk>',update_room , name="room_update"), 

    path('timeline/',timeline,name="timeline"),
    path('occupation/<int:pk>' , occupation , name="occupation"),
    
]
