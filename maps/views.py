from django.shortcuts import render , redirect
from accounts.models import *
from .forms import LocationForm
from django.http import JsonResponse
import json
# Create your views here.

#This function will output the map with a dragable marker that helps the staff user to
#locate their business site on the map
#It will save the longitude and latitude of the marker
def create_house_map(request, pk):
    house = House.objects.get(id = pk)
    location_form = LocationForm(request.POST)

    if location_form.is_valid():
        form = location_form.save(commit=False)
        form.house = house
        form.save()

        return redirect("advert:profile" , request.user.id)
        
    context = {
        'form':location_form,
        'house':house
    }
    return render(request , 'maps/create_house.html',context)

def map_view(request):

    return render(request , 'pages/maps.html' )

def jsonData(request):
    data = list(Location.objects.values())
    house = list(House.objects.values())
    context = [data , house]


    return JsonResponse(context,safe=False)