from django.contrib import admin 
from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    # path('register', views.index, name='register'),
    path('login', views.login, name='login'),
    
]
