from re import template
from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
from django.contrib.auth.views import LogoutView

app_name = "accounts"
# This is a namespace used inside templates 

urlpatterns=[
    path('registration',UserRegisterView.as_view(),name="register"),
    path('accounts/login/',CustomLoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(next_page = 'accounts:home') , name ="logout"),
    path('',home,name="home"),
   
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="registration/reset/password_reset.html"),name="reset_password"),

    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="registration/reset/password_reset_sent.html"),name="password_reset_done"),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="registration/reset/password_reset_form.html"),name="password_reset_confirm"),

    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name="registration/reset/password_reset_done.html"),name="password_reset_complete"),
]

# PasswordResetView -- submit email form

# PasswordResetDoneView -- Email sent success message

# PasswordResetConfirmView -- Link to password Reset in email

# PasswordResetCompleteView -- Password successfully changed message