from django.db import models
from pyclbr import Class

# Create your models here.

class Recipe(models.Model):
    user_name = models.CharField(max_length=100, default='Unknown')
    recipe_name = models.CharField(max_length=200)
    ingredients = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)