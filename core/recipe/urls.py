from . import views

from django.urls import path

urlpatterns = [
    path('donet/', views.Recipe, name='recipe_from'),
]
