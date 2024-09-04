# recipes/models.py
from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.PositiveIntegerField()  
    difficulty = models.CharField(max_length=50)

    def __str__(self):
        return self.name
