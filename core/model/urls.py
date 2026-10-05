from django.urls import include, path

from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
]
