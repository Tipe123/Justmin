from django.http import request
from django.shortcuts import redirect, render ,get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test, login_required

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
Usermodel = get_user_model()

from django.urls import reverse_lazy
from django.views import generic
from .forms import *
from accounts.forms import UserUpdateForm

from accounts.models import *
from accounts.models import UserAccount as User



import datetime
from django.utils import timezone
# Create your views here.

# Here we are going to be creating a crud functionalities of house

# This functionality is used to view the house of the user
# it a read functionality
@login_required(login_url = 'accounts:login')
def house_detail(request,id):

    # number of rooms that belong to house 

    NoRTbTh = Room.objects.filter(house = id)
    rooms = Room.objects.all()
    house_obj = get_object_or_404(House , id = id)

    # occupation = Occupation.objects.all()
    
    taken_rooms = []
    available_rooms = []
    occupied = Occupation.objects.filter(taken = True)
    for rooom in NoRTbTh:
        for ocu in occupied:
            if ocu.room == rooom:
                taken_rooms.append(rooom)
              

    for r_o_o_m in rooms:
        if r_o_o_m not in taken_rooms and r_o_o_m.house == house_obj:
            available_rooms.append(r_o_o_m)
    availabe_length = len(available_rooms)
    
    

    number_of_taken_rooms = Room.objects.filter(house = id).count()
    form = RoomForm(request.POST ,request.FILES)
    context = {'number_of_rooms':number_of_taken_rooms,
                'house':NoRTbTh , 
                'house_obj':house_obj,
                'form':form , 
                'house_id':id,
                'pk_of_owner':house_obj.author.id,
                "available_rooms":available_rooms,
                "taken_rooms":taken_rooms,
                "length":availabe_length
                }

    if form.is_valid():
        room = form.save(commit=False)
        room.house = house_obj
        room.save()
        request.session['price'] = room.price
        request.session['type_of_room'] = room.type_of_room
        
        return redirect(request.path)
    
    form.initial['price'] = request.session.get('price')
    

    return render(request , 'advertisements/house_detail.html',context)

# Now we work on the Update Functionality

def house_update(request , pk):
    item = House.objects.get(id = pk)
    if request.method == "POST":
        house_form = HouseForm(request.POST ,request.FILES, instance=item)

        if house_form.is_valid():
            house_form.save()
            return redirect('advert:profile',request.user.id)
    else:
        house_form = HouseForm(instance= item)

    context = {
        'house_form':house_form
    }

    return render(request , "advertisements/house_update.html",context)

# Now we create a function that delete the house

def delete_house(request , pk):
    item = House.objects.get(id = pk)
    if request.method == 'POST':
        item.delete()
        return redirect("advert:profile" , request.user.id)
    
    return render(request , 'advertisements/delete_house_confirmation.html')

class RoomDetail(generic.DetailView):
    model = Room
    context_object_name = 'room'
    template_name = 'advertisements/room_detail.html'

# We are done with CRUD for house


# Now we begin with CRUD for room

@login_required(login_url = 'accounts:login')
@user_passes_test(lambda u:u.is_staff)
def delete_room(request , pk):
    item = Room.objects.get(id = pk)
    context = {
        'item':item
    }
    if request.method == 'POST':
        item.delete()
        return redirect("advert:profile" ,request.user.id)
    return render(request , "advertisements/room_delete.html" ,context)

def update_room(request,pk):
    item = Room.objects.get(id = pk)
    if request.method == "POST":

        room_form = RoomForm(request.POST ,request.FILES, instance=item)
        
        if room_form.is_valid():
            room_form.save()
            return redirect("advert:profile",request.user.id)
    else:
        room_form = RoomForm(instance= item)
    context = {
        'room_form':room_form
    }

    return render(request , "advertisements/room_update.html",context)
# Has included a functionality of adding a house 
# It also shows the profile of the house
def profile_view(request , pk):
    
    
    
    house_owner = User.objects.get(id = pk)
    profile_item = Profile.objects.get(id = pk)
    form = HouseForm(request.POST ,request.FILES)
    now = datetime.datetime.today
    context = {
        'now':now,
        'house_owner':house_owner,
        'form':form ,
        'pk_of_owner':pk,
        'username':house_owner,
        'profile_item':profile_item,
    }
    
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()

      
        return redirect(request.path)

    
    return render(request, "pages/profile.html",context)

#Now we create a function to edit the profile of user
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST , instance=request.user)
        profile_form = ProfileUpdateForm(request.POST , request.FILES , instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('advert:profile',request.user.id)
        
    else:
        user_form = UserUpdateForm(instance= request.user)
        profile_form = ProfileUpdateForm(instance= request.user.profile)
    
    context = {
        'user_form':user_form,
        'profile_form':profile_form,
    }
    return render(request , "advertisements/update_profile.html",context)



# We create a timeline functionality to output all the houses to our clients

def timeline(request):
    houses = House.objects.all()
    paginator = Paginator(houses, 5) # Show 25 contacts per page
    
    page = request.GET.get('page',1)
    try:
        house_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        house_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        house_page = paginator.page(paginator.num_pages)
    
    context = {
        'house_page': house_page,
        'houses':houses
    }

    return render(request,'pages/timeline.html',context)


def occupation(request,pk):
    occupation_form = OccupationForm(request.POST)
    room_obj = get_object_or_404(Room,id = pk)
        
    if occupation_form.is_valid():
        post = occupation_form.save(commit=False)
        post.owner = request.user
        post.room = room_obj
        post.taken = True
        post.save()
        return redirect('advert:profile',request.user.id)

    context =  {
            'form':occupation_form
        }
    return render(request , 'advertisements/occupation.html',context)



#This function will output the map with a dragable marker that helps the staff user to
#locate their business site on the map
#It will save the longitude and latitude of the marker

def map_view(request):

    return render(request , 'pages/maps.html' )