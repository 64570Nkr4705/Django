from django.urls import path
from ProyectoWebApp import views

urlpatterns = [
    path('home', views.home, name='Home'),
]