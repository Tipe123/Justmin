from django.db.models import fields
from .models import *
from django import forms
from accounts.models import *

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        exclude = ['author']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        exclude = ['house']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','main_picture','profile_picture']


class OccupationForm(forms.ModelForm):
    
    class Meta:
        model = Occupation
        fields = ('set_move_in_date',)