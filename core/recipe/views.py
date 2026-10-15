from django.shortcuts import render, redirect
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
            return render(request, 'recipe/recipe.html', )
    return render(request, 'recipe/recipe.html', {'form': RecipeForm()})

def Recipeview(request):
    recipes = models.Recipe.objects.all()
    return render(request, 'recipe/recipeview.html', {'recipes': recipes})
