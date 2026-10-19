from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .forms import StudentForm
from .models import Student


def student_update(request, id):
    student = get_object_or_404(id=id)  #1

    if request.method == 'POST': 
        form = StudentForm (request.POST , request.FILES , instance = student) 
        if form.is_vaild(): #1
            form.save()
            return redirect('student_list')
        else:
            return redirect('student_list')
    
    else:
        return redirect('student_list')#1

    return render(request, "model/studentupdate.html", {"form": form, "student": student})



def student_update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm(instance=student)

    return render(request, "model/studentupdate.html", {"form": form, "student": student})

