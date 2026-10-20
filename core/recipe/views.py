from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
from .form import RecipeForm
from django.urls import reverse
from . import models
# Create your views here.


def recipehome (request):
    return render(request, 'recipe/recipehome.html')

def Recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'recipe/addrecipe.html', )
    return render(request, 'recipe/addrecipe.html', {'form': RecipeForm()})

def Recipeview(request):
    recipes = models.Recipe.objects.all()
    return render(request, 'recipe/viewrecipe.html', {'recipes': recipes})

def recipe_delete(request , id):
    recipe = get_object_or_404(Recipe , id=id)
    recipe.delete()
    return redirect('Recipeview')
