from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .models import UserAccount
from .forms import   SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin 
import datetime
from django.utils import timezone
from .models import *

# Create your views here.

class UserRegisterView(generic.FormView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('advert:timeline')

    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request , user)
        return super(UserRegisterView, self).form_valid(form)
        
    def get(self , *args , **kwargs):
        if self.request.user.is_authenticated:
            return redirect('advert:timeline')
        return super(UserRegisterView,self).get(*args,**kwargs)

class CustomLoginView(LoginView):
    fields = '__all__'
    redirect_authenticated_user = True
    now = datetime.datetime.now
    now = timezone.now()
    
    def get_success_url(self):
	    return reverse_lazy('advert:timeline')
    
    def get_context_data(self,*args,**kwargs):
        now = datetime.datetime.today
        context = super(CustomLoginView , self).get_context_data(*args,**kwargs)
        context ={'time':now}
        
        return context
        


class UserEditView(generic.UpdateView):
    model = UserAccount
    template_name = 'registration/edit_profile.html'
    fields = ('is_staff',)
    success_url = reverse_lazy('accounts:home')

    def get_object(self):
        return self.request.user

    


def home(request,*arg,**kwarg):
    now = datetime.datetime.today

    return render(request,'pages/index.html', {"time":now})




