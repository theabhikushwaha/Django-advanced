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

def student_delete(requset, id):
    queryset = get_object_or_404(Student, id=id)
    queryset.delete()
    return redirect("student_list")

def student_update(request, id):
    querset = get_object_or_404(Student, id=id)
    context = {student_list:querset}
    return render(request, 'studentupdate.html' , context)