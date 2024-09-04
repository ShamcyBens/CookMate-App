from django.contrib import admin 
from .views import *
from django.urls import path, include
from . import views


urlpatterns = [
    path('recipe_list', views.recipe_list, name='recipe_list'),
    path('recipe_detail', views.recipe_detail, name='recipe_detail'),
    
]
