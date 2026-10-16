from django.shortcuts import redirect, render

from . import models
from .forms import StudentForm


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

# def student_list(request):
#     students = models.Student.objects.all()
#     return render(
#         request,
#         "model/studentlist.html",
#         {"students": students},
#     )

def student_list (request):
	student = models.Student.objects.all()
	
	return render(request,
		"model/studentlist.html",
	    {"students": student},
        )


