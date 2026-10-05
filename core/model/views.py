from django.shortcuts import render

# Create your views here.
from  . import models


def student_list(request):
    if request.method == 'GET':
        students = models.Student.objects.all()
        return render(request, 'model/student.html', {'students': students})
    return render(request, 'model/student.html', {'students': []})

