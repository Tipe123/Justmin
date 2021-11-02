from django import forms
from django.db.models import fields
from accounts.models import *

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        exclude = ['house','created_at']