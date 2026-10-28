from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
from .form import RecipeForm
from django.urls import reverse
from . import models
from .models import Recipe
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def recipehome (request):
    return render(request, 'recipe/recipehome.html')

def recipes_add(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Recipe added.")
            return redirect('recipehome')
    return render(request, 'recipe/addrecipe.html', {'form': RecipeForm()})

def recipeview(request):
    recipes = models.Recipe.objects.all()
    return render(request, 'recipe/viewrecipe.html', {'recipes': recipes})

@require_POST
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe ,pk=pk)
    recipe.delete()
    return redirect('recipe_view')
