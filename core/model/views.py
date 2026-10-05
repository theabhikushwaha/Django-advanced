from django.shortcuts import redirect, render

from . import models
from .forms import StudentForm


def student_list(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm()

    students = models.Student.objects.all()
    return render(
        request,
        "model/student.html",
        {"form": form, "students": students},
    )
