from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpResponseRedirect , HttpResponseNotAllowed
from django.urls import reverse
from .forms import RecipeForm


def abhi(request):
    return render(request, 'home/abhi.html')

def home(request):
    return render(request, 'home/home.html')

def contact(request):
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def view_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Recipe submitted successfully!")
    else:
        form = RecipeForm()
    return render(request, 'home/recipe.html', {'form': form})



def error_404_view(request, exception):
    return render(request, 'home/404.html', status=404)

