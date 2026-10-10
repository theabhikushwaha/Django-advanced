from . import views

from django.urls import path

urlpatterns = [
    path('donet/', views.recipe_from, name='recipe_from'),
]
