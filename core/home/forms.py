from django import forms 
from . import models

class RecipeForm(forms.ModelForm):
    class Meta:
        model = models.Recipe
        fields = ['recipe_name', 'ingredients', 'description', 'image']

