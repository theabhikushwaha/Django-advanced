from django.db import models

# Create your models here.

class Recipe(models.Model):
    user_name = models.CharField(max_length=100, default='Unknown', blank=True)
    recipe_name = models.CharField(max_length=200)
    ingredients = models.TextField(blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
