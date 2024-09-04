# recipes/views.py
from django.shortcuts import render
from .models import *

def ingredient_list(request):
    recipes = Ingredients.objects.all()  
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})


def ingredient_detail(request, pk):
    recipe = Ingredients.objects.get(pk=pk)  
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
