from django.contrib import admin 
from . import views
from django.urls import path


urlpatterns = [
path('ingredient_list', views.ingredient_list, name= 'ingredient_list'),
    
]
