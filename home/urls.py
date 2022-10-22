from django.contrib import admin
from django.urls import path
from home import views
from django.urls import path
#from django.contrib.auth import views as auth_views



urlpatterns = [
    path("",views.first,name='home'),
    path("login",views.login,name='login'),
    path("index",views.index,name='index'),
    path('python_funct', views.python_funct, name='python_funct'),
    ]