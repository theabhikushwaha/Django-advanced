from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .forms import StudentForm
from .models import Student

def student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_add")
    else:
        form = StudentForm()

    students = models.Student.objects.all()
    return render(
        request,
        "model/studentadd.html",
        {"form": form, "students": students},
    )

def student_list(request):
    students = models.Student.objects.all()
    return render(
        request,
        "model/studentlist.html",
        {"students": students},
    )

def delete_student(request, pk):
    if request.method == "POST":
        student = get_object_or_404(Student, pk=pk)
        student.delete()
    return redirect("student_list")