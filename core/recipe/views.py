from django.shortcuts import render

from . import models
# Create your views here.

def recipe_from(request):
    if request.method == 'POST':
        form = models.RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'recipe/recipe.html', {'message': 'Recipe submitted successfully!'})     
    return render(request, 'recipe/recipe.html')
