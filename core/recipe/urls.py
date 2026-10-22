from core import settings
from . import views
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    path('', views.recipehome, name='recipehome'),
    path('add/', views.Recipes, name='recipe_form'),
    path('view/', views.Recipeview, name='recipe_view'),
    path('recipe_delete/<int:id>', views.recipe_delete , name='recipe_delete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
