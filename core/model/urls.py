from django.urls import include, path

from . import views

urlpatterns = [
    path('students/', views.student_add, name='student_add'),
    path('students/list/', views.student_list, name='student_list'),
    path("delete/<int:pk>/", views.student_delete, name="student_delete"),
]
