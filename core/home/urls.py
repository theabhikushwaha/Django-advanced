from django.contrib import admin
from django.urls import include, path

from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('abhi/', views.abhi, name='abhi'),
    path('recipe/', views.view_recipe, name='view_recipe'),
]
