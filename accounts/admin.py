from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import *
# Register your models here.

Usermodel = get_user_model()
admin.site.register(Usermodel)