# recipes/views.py
from django.shortcuts import render
from .models import *

def recipe_list(request):
    recipes = Recipe.objects.all()  
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})


def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)  
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
