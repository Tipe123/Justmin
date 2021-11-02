from django.urls import path,include
from .views import *

app_name = "map"

urlpatterns=[
    path('maps/',map_view , name="map"),
    path('house_create/<int:pk>/',create_house_map , name="create_house_map"),
    path('json/',jsonData , name="json")
]