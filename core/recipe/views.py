from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
from .form import RecipeForm
from django.urls import reverse


from . import models
# Create your views here.

def recipe_from(request):
    if request.method == 'POST':
        form = models.RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'recipe/recipe.html', {'message': 'Recipe submitted successfully!'})     
    return render(request, 'recipe/recipe.html')
